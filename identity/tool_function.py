"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# 定义要匹配的关键字，根据实际情况，去掉O和I
keywords = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
            'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '藏', '川', '鄂', '甘', '赣', '贵', '桂', '黑', '沪', '吉', '冀',
            '津', '晋', '京', '辽', '鲁', '蒙', '闽', '宁', '青', '琼', '陕',
            '苏', '皖', '湘', '新', '渝', '豫', '粤', '云', '浙']


# 显示图片
def show_img(win_name, img):
    cv2.imshow(win_name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# 显示彩色图片
def show_color(img):
    b, g, r = cv2.spilt(img)
    img = cv2.merge([r, g, b])
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()


# plt显示灰度图片
def show_gray(img):
    plt.imshow(img, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 图像去噪灰度处理
def gauss_img(img):
    img = cv2.GaussianBlur(img, (3, 3), 0)
    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return new_img
    # return img


# 假设一个车牌的长宽比在2.8:1到4：1之间，用该标准来判断是不是车牌轮廓
def judge_plate(width, height):
    if (width > (height * 2.8)) and (width < (4.5 * height)):
        return True
    else:
        return False


# 假设车牌中的字长宽比符合1.8：1到3.5：1之间，用该标准来判断是不是字符轮廓
def judge_word(width, height):
    if (height > (width * 1.8)) and (height < (3.5 * width)):
        return True
    else:
        return False


# 提取车牌中的信息
def text_extract(car_plate):
    origin_plate = car_plate.copy()
    car_plate = gauss_img(car_plate)
    # 自适应阈值处理
    ret, car_plate = cv2.threshold(car_plate, 0, 255, cv2.THRESH_OTSU)
    # show_gray(car_plate)
    # identity_massage(car_plate)
    # 计算二值图像黑白点的个数，处理其他车牌颜色的问题，让车牌号码始终为白色
    white_area = 0
    black_area = 0
    height, width = car_plate.shape
    # print(car_plate.shape)
    for i in range(height):
        for j in range(width):
            if car_plate[i, j] == 255:
                white_area += 1
            else:
                black_area += 1

    # 如果白色是背景的话，把它反转过来
    if white_area > black_area:
        ret, car_plate = cv2.threshold(car_plate, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        # show_gray(car_plate)

    # 使白色字膨胀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 4))  # 调整x，y，让单独一个字连在一起
    car_plate = cv2.dilate(car_plate, kernel)
    # show_gray(car_plate)

    # 轮廓检测
    # cv2.RETR_EXTERNAL表示只检测外轮廓
    # cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
    contours, hierarchy = cv2.findContours(car_plate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 绘制轮廓
    car_plate = origin_plate.copy()
    cv2.drawContours(car_plate, contours, -1, (0, 255, 0), 2)
    # show_gray(car_plate)

    # 筛选出各个字符的位置的轮廓, 加到列表text里
    text = []
    for con in contours:
        rectangle = cv2.boundingRect(con)
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]

        # 记录每个轮廓的左上角坐标和围成的矩形的长宽
        word = [x, y, width, height]
        text.append(word)

    # 确保轮廓字符是按左到右的顺序排序的
    text = sorted(text, key=lambda l: l[0], reverse=False)
    # print('text :\n', text)

    plate_img = []
    for word in text:
        if judge_word(word[2], word[3]):
            # 把每个字单独截取出来
            word_img = origin_plate[word[1]:word[1] + word[3], word[0]:word[0] + word[2]]
            # show_gray(word_img)
            plate_img.append(word_img)  # 保存每个字

    return plate_img


# 读取一个文件夹下的所有图片，输入参数是文件名
def read_directory(directory_name):
    refer_img = []
    # 为了匹配图片，拿出需要匹配的图片模板
    for filename in os.listdir(directory_name):
        refer_img.append(directory_name + "/" + filename)

    return refer_img


# 所有模板，但是效率低
def get_all_words_list():
    all_words = []
    for i in range(0, 64):
        word = read_directory('./refer_img/' + keywords[i])
        all_words.append(word)
    return all_words


# 中文模板列表（只匹配车牌的第一个字符）
def get_chinese_words_list():
    chinese_words = []
    for i in range(34, 64):
        c_word = read_directory('D:\\Appication\\data\\DIPtestdata\\refer\\' + keywords[i])
        chinese_words.append(c_word)
    return chinese_words


# 英文模板列表（只匹配车牌的第二个字符）
def get_eng_words_list():
    eng_words = []
    for i in range(10, 34):
        e_word = read_directory('D:\\Appication\\data\\DIPtestdata\\refer\\' + keywords[i])
        eng_words.append(e_word)
    return eng_words


# 英文和数字模板列表（匹配车牌后面的字符）
def get_eng_num_words_list():
    eng_num_words = []
    for i in range(0, 34):
        word = read_directory('D:\\Appication\\data\\DIPtestdata\\refer\\' + keywords[i])
        eng_num_words.append(word)
    return eng_num_words


# 读取一个模板与图片进行匹配，返回相关性得分，越大效果越好
def template_score(template_word, origin_img):
    # fromfile()函数读回数据时需要用户指定元素类型，并对数组的形状进行适当的修改
    template_img = cv2.imdecode(np.fromfile(template_word, dtype=np.uint8), 1)

    # 对读进来的模板图片进行处理
    template_img = gauss_img(template_img)  # 高斯去噪，灰度处理
    ret, template_img = cv2.threshold(template_img, 0, 255, cv2.THRESH_OTSU)  # 自适应阈值处理
    img = origin_img.copy()

    # 不能直接匹配，要使两张图片具有相同的尺寸
    height, width = img.shape
    template_img = cv2.resize(template_img, (width, height))  # 把图片尺寸设成一样的

    # 调用模板匹配函数matchTemplate，用cv2.TM_CCOEFF的算法进行匹配，返回值越大，表示越相关
    result = cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF)
    return result[0][0]


# 最后显示识别结果的界面
def show_result(str_res):
    root_ = Tk()

    frame1_ = Frame(root_)
    frame2_ = Frame(root_)
    frame3_ = Frame(root_)

    var = StringVar()
    var.set(str_res)

    # img = PhotoImage(file='./car_plate.png')

    # Label(frame1_, image=img).grid(row=1, column=1, sticky=W, padx=50, pady=30)
    # Label(frame2_, textvariable=var).grid(row=2, column=3, sticky=E, padx=50, pady=50)

    # Button(frame2, text='点击启动', command=callback2).grid(row=2, column=0, sticky=E, padx=50, pady=50)
    Button(frame2_, text='退出系统', width=10, command=root_.quit).grid(row=2, column=1, sticky=W, padx=50, pady=50)
    Button(frame2_, text='结果如右所示', width=20).grid(row=2, column=2, sticky=E, padx=50, pady=50)
    Button(frame2_, text=str_res, width=50).grid(row=2, column=3, sticky=E, padx=50, pady=50)

    frame1_.pack(padx=100, pady=50)
    frame2_.pack(padx=50, pady=50)
    frame3_.pack(padx=10, pady=10)

    mainloop()
