import cv2
import numpy as np
"""
Created on Wed Jan 22 10:56:47 2020

@author: Dr. Omer Ishaq
"""

'''
Lets first load the image
'''
img_color = cv2.imread('redcar.jpg')
img_gray = cv2.imread('redcar.jpg',0)

'''
Discuss the dimensionality of the image.
'''

sizes_color = np.shape(img_color)
sizes_gray = np.shape(img_gray)

''' 
write results to files
'''
cv2.imwrite('output_color.jpg', img_color)
cv2.imwrite('output_gray.jpg', img_gray)

#red_channel = img_color[:,:,2]
#temp_img = np.copy(img_color)
#temp_img[:,:,0] = red_channel
#temp_img[:,:,1] = red_channel
#temp_img[:,:,2] = red_channel
#cv2.imwrite('hassan.jpg', temp_img)

'''
Convert color to gray
'''
img_transform_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output_transform_gray.jpg', img_transform_gray)

'''
Isolate red channel
'''
img_red = img_color[:,:,2]
img_blue = img_color[:,:,0]
cv2.imwrite('output_red_channel.jpg', img_red)
cv2.imwrite('output_blue_channel.jpg', img_blue)

''' 
Discuss the uint8 coding and ranges
'''

''' Darken an image'''
img_dark = img_gray - 50
cv2.imwrite('output_dark.jpg', img_dark)

img_dark = np.float32(img_gray)
img_dark = img_dark - 32
img_dark[img_dark < 0] = 0
img_dark = np.uint8(img_dark)
cv2.imwrite('output_dark_correct.jpg', img_dark)

''' Convert to HSV '''
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)



