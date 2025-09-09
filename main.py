import cv2 as cv 
import mediapipe as mp 
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 
# Accessing the hands object in mediapipe
mp_hands = mp.solutions.hands 
hand = mp_hands.Hands()

# Drawing and tracking the hand landmarks
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Captures frames in camera and turns into video
capture = cv.VideoCapture(1)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        ret, img = capture.read()
        

        # Converts to RGB format and processes the hand
        RGB_frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                print(hand_landmark)
                mp_drawing.draw_landmarks(RGB_frame, 
                                        hand_landmark, 
                                        mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing_styles.get_default_hand_landmarks_style(),
                                        mp_drawing_styles.get_default_hand_connections_style())
        flipped = cv.flip(RGB_frame, 1)

        cv.imshow('img', flipped)
        k = cv.waitKey(30) & 0xff
        if k == ord('q'):
            break
