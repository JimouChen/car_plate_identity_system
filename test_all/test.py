"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import pytesseract
import cv2

# 1.引入Tesseract程序
pytesseract.pytesseract.tesseract_cmd = r'D:\Appication\PyCharm\TesseractOCR\tesseract.exe'
image = cv2.imread('D:/testocr.png')
print(image)

# 2.识别图片文字
code = pytesseract.image_to_string(image)
print(code)
