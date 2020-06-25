"""
# @Time    :  2020/6/26
# @Author  :  Jimou Chen
"""
import cv2
import numpy as np
import tensorflow as tf

car_plate_img = cv2.imread('./car_plate_photo/1.jpg', cv2.IMREAD_GRAYSCALE)
print(car_plate_img)