# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:56:39 2020

@author: Mayra Ahmad
"""
import cv2
import numpy as np

img_color_blue = cv2.imread('blue.jpg',1)
img_color_red = cv2.imread('red.jpg',1)
'''
converting images to grayscale
'''
img_gray_blue = cv2.imread('blue.jpg',0)
img_gray_red = cv2.imread('red.jpg',0)
'''
Checking the dimensionality of the image.
'''

sizes_color_blue = np.shape(img_color_blue)
sizes_color_red = np.shape(img_color_red)
sizes_gray_blue = np.shape(img_gray_blue)
sizes_gray_red = np.shape(img_gray_red)

''' 
writing results to files
'''
#cv2.imwrite('output_color_blue.jpg', img_color_blue)
#cv2.imwrite('output_color_red.jpg', img_color_red)
cv2.imwrite('output_color_blue.jpg', img_gray_blue)
cv2.imwrite('output_color_red.jpg', img_gray_red)
