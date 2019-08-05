import cv2
import numpy as np

vidObject = cv2.VideoCapture(0)

while True:
    ret, frame = vidObject.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('frame1', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vidObject.release()
cv2.destroyAllWindows()