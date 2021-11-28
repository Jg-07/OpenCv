## This is my complete OpenCV Session

## Reading Images and Videos

import cv2 as cv

img = cv.imread('res/Lenna.png')
imgBW = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
imgBlur = cv.GaussianBlur(img,(7,7),0)
imgCan = cv.Canny(img,100,100)

read = cv.bitwise_and(img,imgRGB)
read2 = cv.bitwise_or(img,imgRGB)
read3 = cv.bitwise_xor(img,imgRGB)
read4 = cv.bitwise_not(img,imgRGB)

cv.imshow('BGR',img)
cv.imshow('RGB',imgRGB)
cv.imshow('BA',read)
cv.imshow('BO',read2)
cv.imshow('BX',read3)
cv.imshow('BN',read4)
cv.imshow('Original',img)
cv.imshow('B/W',imgBW)
cv.imshow('Blur',imgBlur)
cv.imshow('Canny',imgCan)

cv.waitKey(0)


