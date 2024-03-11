import cv2 as cv
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt2 
import numpy as np

path = "cat.jpg" #Reffering the path of the image
image = cv.imread(path) #Reading the image
cv.imshow('image', image) #Showing the original image

rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB) #Changin the color from BGR to RGB
cv.imshow('rgb', rgb) #Showing the changed image color
plt.imshow(rgb) #Showing the changed image color (rgb) into matplotlib version

plt.show() 
cv.waitKey(0)