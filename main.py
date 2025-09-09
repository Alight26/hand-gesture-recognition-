import cv2 as cv 
import mediapipe as mp 
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 


# Captures frames in camera and turns into video
capture = cv.VideoCapture(0)

# Accessing the hands object in mediapipe
mp_hands = mp.solutions.hands 
hand = mp_hands.Hands()

while True:
    ret, img = capture.read()
    flipped = cv.flip(img, 1)


    # Converts to RGB format and processes the hand
    RGB_frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hand.process(RGB_frame)
    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            print(hand_landmark)







    cv.imshow('img', flipped)
    k = cv.waitKey(30) & 0xff
    if k == ord('q'):
        break
