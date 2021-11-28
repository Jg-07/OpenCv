import cv2 as cv

video = cv.VideoCapture(0)
video.set(3,640)
video.set(4,480)
video.set(10,60)

while True:
    success,img = video.read()
    cv.imshow("Video",img)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break