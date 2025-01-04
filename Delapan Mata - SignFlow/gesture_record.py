import mediapipe as mp
import cv2
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

data = []
labels = []

gestures = {'A': 0, 'B': 1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmark_array = []
            for lm in hand_landmarks.landmark:
                landmark_array.extend([lm.x, lm.y, lm.z])

            cv2.putText(frame, "Press key the abjad to save", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('a'):
                data.append(landmark_array)
                labels.append(gestures['A'])
                print("Saved gesture: A")

            elif key == ord('b'):
                data.append(landmark_array)
                labels.append(gestures['B'])
                print("Saved gesture: B")

            elif key == ord('c'):
                    data.append(landmark_array)
                    labels.append(gestures['C'])
                    print("Saved gesture: C")
                    
            elif key == ord('d'):
                    data.append(landmark_array)
                    labels.append(gestures['D'])
                    print("Saved gesture: D")

            elif key == ord('e'):
                    data.append(landmark_array)
                    labels.append(gestures['E'])
                    print("Saved gesture: E")

            elif key == ord('f'):
                    data.append(landmark_array)
                    labels.append(gestures['F'])
                    print("Saved gesture: F")

            elif key == ord('g'):
                    data.append(landmark_array)
                    labels.append(gestures['G'])
                    print("Saved gesture: G")

            elif key == ord('h'):
                    data.append(landmark_array)
                    labels.append(gestures['H'])
                    print("Saved gesture: H")

            elif key == ord('i'):
                    data.append(landmark_array)
                    labels.append(gestures['I'])
                    print("Saved gesture: I")

            elif key == ord('j'):
                    data.append(landmark_array)
                    labels.append(gestures['J'])
                    print("Saved gesture: J")  

            elif key == ord('k'):
                    data.append(landmark_array)
                    labels.append(gestures['K'])
                    print("Saved gesture: K")

            elif key == ord('l'):
                    data.append(landmark_array)
                    labels.append(gestures['L'])
                    print("Saved gesture: L")

            elif key == ord('m'):
                    data.append(landmark_array)
                    labels.append(gestures['M'])
                    print("Saved gesture: M")

            elif key == ord('n'):
                    data.append(landmark_array)
                    labels.append(gestures['N'])
                    print("Saved gesture: N")

            elif key == ord('o'):
                    data.append(landmark_array)
                    labels.append(gestures['O'])
                    print("Saved gesture: O")

            elif key == ord('p'):
                    data.append(landmark_array)
                    labels.append(gestures['P'])
                    print("Saved gesture: P")

            elif key == ord('q'):
                    data.append(landmark_array)
                    labels.append(gestures['Q'])
                    print("Saved gesture: Q")

            elif key == ord('r'):
                    data.append(landmark_array)
                    labels.append(gestures['R'])
                    print("Saved gesture: R")

            elif key == ord('s'):
                    data.append(landmark_array)
                    labels.append(gestures['S'])
                    print("Saved gesture: S")

            elif key == ord('t'):
                    data.append(landmark_array)
                    labels.append(gestures['T'])
                    print("Saved gesture: T")

            elif key == ord('u'):
                    data.append(landmark_array)
                    labels.append(gestures['U'])
                    print("Saved gesture: U")

            elif key == ord('v'):
                    data.append(landmark_array)
                    labels.append(gestures['V'])
                    print("Saved gesture: V")

            elif key == ord('w'):
                    data.append(landmark_array)
                    labels.append(gestures['W'])
                    print("Saved gesture: W")

            elif key == ord('x'):
                    data.append(landmark_array)
                    labels.append(gestures['X'])
                    print("Saved gesture: X")

            elif key == ord('y'):
                    data.append(landmark_array)
                    labels.append(gestures['Y'])
                    print("Saved gesture: Y")

            elif key == ord('z'):
                    data.append(landmark_array)
                    labels.append(gestures['Z'])
                    print("Saved gesture: Z")                                                                                                             
                    
    cv2.imshow("Capture Gestures", frame)

    if cv2.waitKey(1) & 0xFF == ord('`'):
        break

cap.release()
cv2.destroyAllWindows()

np.save('gestures_data.npy', np.array(data))
np.save('gestures_labels.npy', np.array(labels))
