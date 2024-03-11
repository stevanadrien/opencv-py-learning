import cv2 as cv
path = 'cat.jpg'
img = cv.imread(path)
cv.imshow('Cat', img)

#MAKING AN IMAGE TO GREYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', gray)

#BLUR AN IMAGE
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow('canny', canny)
#YOU CAN REDUCE THE CANNY DETAIL BY PASSING THE BLUR TO THE CANNY CV.CANNY

#DILATING IMAGE
dilated = cv.dilate(img, (3,3), iterations=1)
cv.imshow('dilate', dilated)

#ERODING IMAGE
eroded = cv.erode(img, (3,3), iterations=1 )
cv.imshow('eroded', eroded)

#RESIZE IMAGE
resized = cv.resize(img, (200,100), interpolation=cv.INTER_AREA)
cv.imshow('resizedd', resized)

#CROP IMAGE
crop = img[50:70, 20:50]
cv.imshow("crop",crop)
cv.des
cv.waitKey(0)