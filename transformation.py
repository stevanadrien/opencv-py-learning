import cv2 as cv
import numpy as np
path = 'cat.jpg'
image = cv.imread(path)


def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = [image.shape[1], image.shape[0]]
    return cv.warpAffine(image, transMat, dimensions)
# -x to left
# x to right
# -y to up
# y to down
translated = translate(image, 300, 340)
cv.imshow('translated', translated)
cv.waitKey(0)