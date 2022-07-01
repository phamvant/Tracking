import cv2
import numpy as np

im_lower = np.array([20, 75, 75], dtype="uint8")
im_upper = np.array([35, 255, 255], dtype="uint8")
kernel = np.ones((3, 3), np.uint8)

img_copy = cv2.imread('test.png')
im_hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
im_mask = cv2.inRange(im_hsv, im_lower, im_upper)
im_mask = cv2.morphologyEx(im_mask, cv2.MORPH_OPEN, kernel)
cnts, _ = cv2.findContours(im_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
    cv2.circle(img_copy, (cX, cY), 8, (0, 0, 0), -1)
    cv2.putText(img_copy, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow('a', img_copy)
cv2.waitKey()