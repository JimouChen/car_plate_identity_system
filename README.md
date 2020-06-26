This is a project to identity car plates.
Use OpenCV, Tesseract ... and so on.
import cv2, pytesseract ... and so on

步骤
    https://github.com/UB-Mannheim/tesseract/wiki
    安装 Tesseract
    调用pytesseract直接使用即可，如果没有装中文包，要记得装，要不然识别不了中文。
    记得使用：
    `pytesseract.pytesseract.tesseract_cmd = r'...\tesseract.exe'`
    

