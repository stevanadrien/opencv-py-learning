import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = 'cat.jpg'
img = cv.imread(path)
cv.imshow("image", img)

# MAKING THE PICTURE "NORMAL / OVERALL" BLUR
average = cv.blur(img,(21,21))
cv.imshow("average", average)

# GAUSSIAN BLUR
gauss = cv.GaussianBlur(img, (21,21), 0)
cv.imshow("gaussian", gauss)

# MEDIAN BLUR
median = cv.medianBlur(img,21)
cv.imshow("median", median)
cv.waitKey(0)