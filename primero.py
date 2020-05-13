## simple plantilla para comenzar a leer las capturas de frames


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('face_recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyWindow()
