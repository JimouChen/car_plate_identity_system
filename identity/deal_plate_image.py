"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import cv2
from identity.tool_function import *

img = cv2.imread('./car_plate_photo/1.jpg', cv2.IMREAD_GRAYSCALE)
show_img('123', img)
