# Importing necessary libraries
import cv2 as cv
import matplotlib.pyplot as plt

# Specifying the path to the image file
path = 'cat.jpg'

# Reading the image using OpenCV
img = cv.imread(path)

# Displaying the original image
cv.imshow("image", img)

# Converting the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Displaying the grayscale image
cv.imshow('grey', gray)

# Calculating the histogram of the grayscale image
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# Creating a Matplotlib histogram for visualization
plt.figure()
plt.title('Greyscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

# Showing the Matplotlib histogram
plt.show()

# Waiting for a key press to close the OpenCV windows
cv.waitKey(0)
