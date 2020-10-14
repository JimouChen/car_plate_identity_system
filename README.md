This is a project to identity car plates.
Use OpenCV, Tesseract ... and so on.
import cv2, pytesseract ... and so on

- 步骤
    https://github.com/UB-Mannheim/tesseract/wiki
    安装 Tesseract
    调用pytesseract直接使用即可，如果没有装中文包，要记得装，要不然识别不了中文。
    记得使用：
    `pytesseract.pytesseract.tesseract_cmd = r'...\tesseract.exe'`
    
- 注意事项：
    lang字符串-Tesseract语言代码字符串。如果未指定，则默认为eng！多种语言的示例：lang ='eng + fra'
    
把车牌找到后，我对每个字符进行一一使用Tesseract识别，发现效果不好，所以打算使用大量图片的匹配算法来实现识别。
**最后决定使用opencv自带的模板匹配函数进行识别，结果测试发现这样的正确率较高。**
如果还需要提高准确率，可以采用其他方法：
    CNN
    等...
