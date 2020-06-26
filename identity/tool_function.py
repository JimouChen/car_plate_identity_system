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


# 使用Tesseract进行识别
def identity_massage(car_plate):
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'D:\Appication\PyCharm\tesseract\tesseract.exe'
    # 识别图片文字
    #  code = pytesseract.image_to_string(car_plate, lang='eng+chi_sim+chi_sim_vert+chi_tra+chi_tra_vert')
    # code = pytesseract.image_to_string(car_plate)
    code = pytesseract.image_to_boxes(car_plate, lang='chi_sim')
    print(code)
