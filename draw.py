import cv2 as cv
import numpy as np

blank = np.zeros((400,400,3), dtype='uint8') #MAKING THE BLANK IMAGE
cv.imshow('Blank', blank) #SHOWING THE BLANK IMAGE

blank[100:200] = 0,0,255 #CHANGE THE IMAGE COLOR
cv.imshow('Green', blank)
kotak = cv.rectangle(blank, (0,0),(250,250), (0,255,0), thickness=2)
cv.imshow("lpta", kotak)

text = cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_COMPLEX, 1,(0,255,0),2)
cv.imshow("TEXT", text)
cv.waitKey(0)
cv.destroyAllWindows