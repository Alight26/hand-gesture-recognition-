import cv2 as cv 
import mediapipe as mp 
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 
import pyautogui
# Accessing the hands object in mediapipe
mp_hands = mp.solutions.hands 
hand = mp_hands.Hands()


# Drawing and tracking the hand landmarks
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# This function should detect whether your pointer finger is up

def pointer(hand_landmarks):

    landmarks = hand_landmarks.landmark


    if landmarks[8].y < landmarks[6].y:
        pyautogui.press('space')
        return True

    else:
        return False

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
            for hand_landmarks in result.multi_hand_landmarks:

                mp_drawing.draw_landmarks(RGB_frame, 
                                        hand_landmarks, 
                                        mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing_styles.get_default_hand_landmarks_style(),
                                        mp_drawing_styles.get_default_hand_connections_style())
                is_up = pointer(hand_landmarks)

                if is_up is True:
                    print("It Worked!!!!!!!!!!!!")
                    
                




     
        flipped = cv.flip(RGB_frame, 1)
        # changing back to bgr
        flipped_BGR = cv.cvtColor(flipped, cv.COLOR_RGB2BGR)

        cv.imshow('img', flipped_BGR)
        k = cv.waitKey(30) & 0xff
        if k == ord('q'):
            break






