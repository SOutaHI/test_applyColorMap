import cv2
import sys
import os
import numpy as np

args           = sys.argv
read_file_name = args[1]

color_map_names_list = [
        'autom',
        'born',
        'jet',
        'winter',
        'rainbow',
        'ocean',
        'summer',   
        'spring',   
        'cool',
        'hsv',  
        'pink', 
        'hot']

write_file_name = (read_file_name.split('.'))[0]
img             = cv2.imread(read_file_name)


if not os.path.exists(write_file_name):
    os.mkdir(write_file_name)

image2  = cv2.bitwise_not(img)
im_gray = cv2.imread(read_file_name, cv2.IMREAD_GRAYSCALE)

gray_name   = './' + write_file_name + '/' + write_file_name + '_gray.jpg'
invert_name = './' + write_file_name + '/' + write_file_name + '_invert.jpg'

cv2.imwrite(gray_name,image2)
cv2.imwrite(invert_name,im_gray)

for i in range(len(color_map_names_list)):
    im_gray  = cv2.imread(read_file_name, cv2.IMREAD_GRAYSCALE)
    im_color = cv2.applyColorMap(im_gray, i)

    file_name = './' + write_file_name + '/' + write_file_name + '_' + color_map_names_list[i] + '.jpg'

    cv2.imwrite(file_name,im_color)
