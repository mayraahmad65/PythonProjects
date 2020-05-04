# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:09:37 2020

@author: Mayra Ahmad
"""
import cv2

img_sudoku = cv2.imread('sudoku.jpeg')
img_sudoku_gray = cv2.imread('sudoku.jpeg',0)

cv2.imwrite('output_gray.jpeg', img_sudoku_gray)
''' Global threshold
ret,thresh1 = cv2.threshold(img_sudoku_gray,127,255,cv2.THRESH_BINARY)

cv2.imwrite('output_threshold.jpeg', thresh1)
'''

'''Adaptive threshold'''
th2 = cv2.adaptiveThreshold(img_sudoku_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
             cv2.THRESH_BINARY,11,2)

cv2.imwrite('output_mean.jpeg', th2)

th3 = cv2.adaptiveThreshold(img_sudoku_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
             cv2.THRESH_BINARY,11,2)

cv2.imwrite('output_gaussian.jpeg', th3)