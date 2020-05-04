# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:13:22 2020

@author: Mayra Ahmad
"""
import cv2

img_color_blue = cv2.imread('blue.jpg',1)
img_color_red = cv2.imread('red.jpg',1)

'''
Converting images color to gray
'''
img_transform_gray_blue = cv2.cvtColor(img_color_blue, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output_transform_gray_blue.jpg', img_transform_gray_blue)

img_transform_gray_red = cv2.cvtColor(img_color_red, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output_transform_gray_red.jpg', img_transform_gray_red)

'''
Converting images color to HSV
'''
img_transform_HSV_blue = cv2.cvtColor(img_color_blue, cv2.COLOR_BGR2HSV)
cv2.imwrite('output_transform_HSV_blue.jpg', img_transform_HSV_blue)

img_transform_HSV_red = cv2.cvtColor(img_color_red, cv2.COLOR_BGR2HSV)
cv2.imwrite('output_transform_HSV_red.jpg', img_transform_HSV_red)
