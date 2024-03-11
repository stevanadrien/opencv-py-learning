import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blank = np.zeros((400,400), dtype='uint8') #MAKING AN BLANK CANVAS
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370),255, -1) #DRAWING RECTANGLE TO THE BLANK CANVAS
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) #DRAWING CIRCLE TO THE BLANK CANVAS

cv.imshow('b', rectangle)
cv.imshow('a', circle)

bitwise_and = cv.bitwise_and(rectangle,circle) #BITWISE AND OPERATION
cv.imshow('bitwise', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)  #BITWISE OR OPERATION
cv.imshow('as', bitwise_or)


bitwise_xor = cv.bitwise_xor(rectangle, circle) #BITWISE XOR OPERATION
cv.imshow('as', bitwise_xor)

bitwise_not = cv.bitwise_not(circle) #BITWISE NOT OPERATION
cv.imshow('as', bitwise_not)

cv.waitKey(0)