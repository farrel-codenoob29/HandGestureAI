import cv2
import numpy as np
import tensorflow as tf
import pyttsx3
import mediapipe as mp

model = tf.keras.models.load_model('gesture_model.h5')

cap = cv2.VideoCapture(0)

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

tts_engine = pyttsx3.init()

sentence = ""
recent_predictions = []
recent_confidences = []
frame_buffer_size = 5  

threshold_confidence = 50

add_to_sentence_key = 'a'
clear_sentence_key = 'c'
speak_sentence_key = 't'
space_key = 's'
exit_key = 'q'

cv2.namedWindow("SignFlow", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("SignFlow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    predicted_label = "Tangan Tidak Terdeteksi"
    confidence = 0.0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            
            landmarks = np.array(landmarks).reshape(1, -1)
            predictions = model.predict(landmarks)
            
            predicted_class = np.argmax(predictions[0])
            predicted_label = labels[predicted_class]
            confidence = np.max(predictions[0]) * 100

            recent_predictions.append(predicted_class)
            recent_confidences.append(confidence)

            if len(recent_predictions) > frame_buffer_size:
                recent_predictions.pop(0)
                recent_confidences.pop(0)

            most_common_prediction = max(set(recent_predictions), key=recent_predictions.count)
            avg_confidence = np.mean(recent_confidences)

    cv2.putText(frame, f'Prediksi: {predicted_label} ({confidence:.2f}%)', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, lineType=cv2.LINE_AA)
    
    cv2.putText(frame, f'Kalimat: {sentence}', (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, lineType=cv2.LINE_AA)

    cv2.putText(frame, f'Kontrol: [a:add][s:spasi][c:clear][t:ngomong][q:keluar]', (10, frame.shape[0] - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 1, lineType=cv2.LINE_AA)

    cv2.imshow('SignFlow', frame)

    key = cv2.waitKey(1) & 0xFF  

    if key == ord(add_to_sentence_key):
        if avg_confidence > threshold_confidence:
            sentence += labels[most_common_prediction]
            print(f"Added: {labels[most_common_prediction]} | Confidence: {avg_confidence:.2f}%")
    elif key == ord(space_key):
        sentence += " "
    elif key == ord(clear_sentence_key):
        sentence = ""
    elif key == ord(speak_sentence_key):
        if sentence:
            tts_engine.say(sentence)
            tts_engine.runAndWait()
    elif key == ord(exit_key):
        break

cap.release()
cv2.destroyAllWindows()
