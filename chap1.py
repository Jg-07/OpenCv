## This is my complete OpenCV Session

## Reading Images and Videos

import cv2 as cv
print("Start")
img = cv.imread("./res/Lenna.png")
cv.imshow(img)
cv.waitKey(0)
