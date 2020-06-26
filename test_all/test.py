"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import pytesseract
import cv2
import matplotlib.pyplot as plt

# 1.引入Tesseract程序
pytesseract.pytesseract.tesseract_cmd = r'D:\Appication\PyCharm\tesseract\tesseract.exe'
image = cv2.imread('D:/test3.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('123', image)
pic = plt.figure()
# pic.subplot()
# plt.imshow(image, cmap='gray', interpolation='bicubic')
plt.imshow(image, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()
print(image)

# 2.识别图片文字
# code = pytesseract.image_to_string(image, lang='eng+chi_sim+chi_sim_vert+chi_tra+chi_tra_vert')
code = pytesseract.image_to_string(image, lang='eng')
#code = pytesseract.image_to_boxes(image, lang='eng')
print(code)

