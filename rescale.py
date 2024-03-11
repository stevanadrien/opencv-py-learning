import cv2 as cv
#IMPORTING CV

photo_path = 'cat.jpg' #SHOWING THE PICTURE FILE LOCATION
image = cv.imread(photo_path) #READING THE IMAGE AND ASSIGN THEM INTO AN VARIABLE
cv.imshow('Cat',image) #SHOWING THE IMAGE

def rescaleFrame(frame, scale=0.2): #FUNCTION TO RESCALE WIDTH AND HEIGHT OF THE PICTURE / VIDEO
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

image_resized = rescaleFrame(image) #APPLICATION OF THE FUNCTION AND ASSIGNED IT TO A VARIABLE
cv.imshow("Resized Image", image_resized) #SHOWING THE RESIZED PICTURE

video_path = 'example.mp4' #PATH OF THE VIDEO FILE
capture = cv.VideoCapture(video_path) #READING THE VIDEO FILE AND ASSIGNED IT TO THE VARIABLE
while True: #WHILE LOOPING FOR STOPPING IF PRESSING D
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow("Resized", frame_resized)
    if cv.waitKey(2) & 0xFF==ord('d'):
        break

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture.release()