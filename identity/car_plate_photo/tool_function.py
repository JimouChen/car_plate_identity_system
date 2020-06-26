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
    plt.show()


# plt显示灰度图片
def show_gray(img):
    plt.imshow(img, cmap='gray')
    plt.show()

