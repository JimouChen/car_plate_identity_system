"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import cv2
import matplotlib.pyplot as plt


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
    if (width > (height * 2.8)) and (width < (4 * height)):
        return True
    else:
        return False


# 假设车牌中的字长宽比符合1.8：1到3.5：1之间，用该标准来判断是不是字符轮廓
def judge_word(width, height):
    if (height > (width * 1.8)) and (height < (3.5 * width)):
        return True
    else:
        return False


# 使用Tesseract进行识别
def identity_massage(car_plate):
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'D:\Appication\PyCharm\tesseract\tesseract.exe'
    # 识别图片文字
    # code = pytesseract.image_to_string(car_plate, lang='eng+chi_sim+chi_sim_vert+chi_tra+chi_tra_vert')
    code = pytesseract.image_to_string(car_plate)
    #  code = pytesseract.image_to_boxes(car_plate, lang='chi_sim')
    print(code)


# 提取车牌中的信息
def text_extract(car_plate):
    origin_plate = car_plate.copy()
    car_plate = gauss_img(car_plate)
    # 自适应阈值处理
    ret, car_plate = cv2.threshold(car_plate, 0, 255, cv2.THRESH_OTSU)
    show_gray(car_plate)
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
    print('text :\n', text)

    count = 0
    for word in text:
        if judge_word(word[2], word[3]):
            count += 1
            # 把每个字单独截取出来
            word_img = origin_plate[word[1]:word[1] + word[3], word[0]:word[0] + word[2]]
            show_gray(word_img)
