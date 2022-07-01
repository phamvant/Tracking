from turtle import circle
import cv2
import numpy as np
import glob
 
img_array = []
array_name = []

for filename in glob.glob('D:\\Python\\LAB\\Tracking\\lm\\*.jpg'):
    array_name.append(filename)
    # print(filename)

# for filename in glob.glob('D:\\Python\\LAB\\Baseall\\*.jpg'):
#     if(len(filename) == 32):
#         array_name.append(filename)
#         print(filename)
        
# for filename in glob.glob('D:\\Python\\LAB\\Baseall\\*.jpg'):
#     if(len(filename) == 33):    
#         array_name.append(filename)
#         print(filename)

# for filename in glob.glob('D:\\Python\\LAB\\Baseall\\*.jpg'):
#     if(len(filename) == 34):    
#         array_name.append(filename)
#         print(filename)

# for filename in glob.glob('D:\\Python\\LAB\\Baseall\\*.jpg'):
#     if(len(filename) == 35):    
#         array_name.append(filename)
#         print(filename)


for filename in array_name:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    cv2.circle(img, (int(height / 2), int(width / 2)), 3, (0, 0, 255), -1)
    img_array.append(img)
    cv2.imshow('a', img)
    cv2.waitKey(1)
 
out = cv2.VideoWriter('finalxx.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()