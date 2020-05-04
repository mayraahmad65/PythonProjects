# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:24:51 2020

@author: Mayra Ahmad
"""
import cv2
import numpy as np

img_color_blue = cv2.imread('blue.jpg',1)
img_color_red = cv2.imread('red.jpg',1)

img_transform_HSV_blue = cv2.cvtColor(img_color_blue, cv2.COLOR_BGR2HSV)

blue_lower=np.array([100,150,0],np.uint8)
blue_upper=np.array([140,255,255],np.uint8)
blue=cv2.inRange(img_transform_HSV_blue,blue_lower,blue_upper)

cv2.imwrite('blue_detect.jpg', blue)

img_transform_HSV_red = cv2.cvtColor(img_color_red, cv2.COLOR_BGR2HSV)

red_lower=np.array([170,150,0],np.uint8)
red_upper=np.array([180,255,255],np.uint8)
red=cv2.inRange(img_transform_HSV_red,red_lower,red_upper)

cv2.imwrite('red_detect.jpg', red)

'''
Inrange function
'''
for h in range(170,180) or (0,10):
    red_lower=np.array([h,150,0],np.uint8)
    red_upper=np.array([h,255,255],np.uint8)
    red=cv2.inRange(img_transform_HSV_red,red_lower,red_upper)
cv2.imwrite('output_transform_red.jpg', red)
