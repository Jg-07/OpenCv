## Image Manupulations

# > Resize
# > Crop
# > Masking
# > Enhancing
# > Rotating

# RESIZE :

import cv2 as cv

img = cv.imread('../res/Lenna.png')

resized = cv.resize(img,(100,200))

cv.imshow('resized',resized)

cv.waitKey(0)