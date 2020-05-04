# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:45:25 2020

@author: Mayra Ahmad
"""

import cv2

img_sudoku = cv2.imread('sudoku.jpeg')
img_sudoku_gray = cv2.imread('sudoku.jpeg',0)

cv2.imwrite('output_gray.jpeg', img_sudoku_gray)

for i in range(w):
    for j in range(h):
        tmp_2d[i][j] = src_1d[i+(j*i_w)] & 0x000000ff

def threshold(image,b_value,thresh_mean,thresh_binary): 
    for i in range(0,height):
        for j in range(0,width):
            mean = 0
            count = 0
            for k in range(0,size):
                for l in range(0,size):
                    mean = mean + tmp_2d[(i-(int[(size/2)])+k)][j-(int[(size/2)])+l)]
                    count +=1
            mean = (mean/count) - con
            
            
    