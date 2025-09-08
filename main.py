import cv2 as cv 
import mediapipe as mp 
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 


capture = cv.VideoCapture(1)

while True:
    ret, img = capture.read()
    flipped = cv.flip(img, 1)



    cv.imshow('img', flipped)
    k = cv.waitKey(30) & 0xff
    if k == ord('q'):
        break
