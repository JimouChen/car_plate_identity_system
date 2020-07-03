"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import cv2
from identity.tool_function import *
import identity.GUI as UI

# 从界面获取要识别的图片
pic_num = UI.e1.get()
img = cv2.imread('./car_plate_photo/'+pic_num+'.jpg')

# img = cv2.imread('./car_plate_photo/2.jpg')
# img = cv2.imread('./car_plate_photo/9.jpg')
img1 = img.copy()
gray_img = gauss_img(img)  # 高斯去噪
# show_gray(img)

# sobel算子边缘检测
sobel_x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0)
img = cv2.convertScaleAbs(sobel_x)  # 转回uint8
# show_gray(img)

# 自适应阈值处理
ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
show_gray(img)

# 形态学处理
# 闭运算,把白色部分练成整体
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 5))  # 把x方向的膨胀设为20，y的设为10
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=4)  # 迭代次数设到合适
show_gray(img)
# 去除一些小的白点
# kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (350, 1))
# kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 130))
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))

# 膨胀，腐蚀
img = cv2.dilate(img, kernelX, iterations=1)
img = cv2.erode(img, kernelX, iterations=1)
# 腐蚀，膨胀
img = cv2.erode(img, kernelY, iterations=1)
img = cv2.dilate(img, kernelY, iterations=1)
# show_gray(img)

# 中值滤波去除噪点
img = cv2.medianBlur(img, 25)  # 15
# show_gray(img)

# 轮廓检测
# cv2.RETR_EXTERNAL表示只检测外轮廓
# cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(hierarchy)
# 绘制轮廓
cv2.drawContours(img1, contours, -1, (0, 255, 0), 5)  # 30
# show_gray(img1)

# 上一次截取的字符清空
count_list = read_directory('./every_word')
count_words = len(count_list)
for i in range(1, count_words + 1):
    os.remove('./every_word/' + str(i) + '.png')

# 选出车牌的轮廓
for con in contours:
    # cv2.boundingRect用一个最小的矩形把找到的轮廓圈起来
    # 返回值rectangle是个包含矩形左上角x,y坐标以及长宽的列表
    rectangle = cv2.boundingRect(con)
    x = rectangle[0]
    y = rectangle[1]
    width = rectangle[2]
    height = rectangle[3]

    # print('x={},y={},w={},h={}'.format(x, y, width, height))

    # 截取出符合车牌长宽要求的轮廓区域图片
    if judge_plate(width, height):
        car_plate = img1[y:y + height, x:x + width]  # 截取出车牌轮廓
        show_gray(car_plate)
        cv2.imwrite('./car_plate.png', car_plate)
        print('截取成功')
        # 将每个字提取出来,放到列表里
        word_img = text_extract(car_plate)

        for i in range(1, len(word_img) + 1):
            cv2.imwrite('./every_word/' + str(i) + '.png', word_img[i - 1])  # 保存
            show_gray(word_img[i - 1])
        break
