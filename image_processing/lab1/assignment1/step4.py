# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:53:51 2020

@author: Mayra Ahmad
"""

import cv2

img_color_red = cv2.imread('red.jpg')
img_color_blue = cv2.imread('blue.jpg')

img_red_Transformed = cv2.imread('red_detect.jpg')
img_blue_Transformed = cv2.imread('blue_detect.jpg')

im_red_concat = cv2.hconcat([img_color_red,img_red_Transformed])
cv2.imwrite('Concate_Img_red.jpg', im_red_concat)

im_blue_concat = cv2.hconcat([img_color_blue,img_blue_Transformed])
cv2.imwrite('Concate_Img_blue.jpg', im_blue_concat)