import cv2, time

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"E:\Python\OpenCVLearning\OpenCV\haarCascades\haarcascade_frontalface_default.xml")



while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(grey_frame, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        resize = cv2.resize(img, (int(img.shape[1]), int(img.shape[1])))

        cv2.imshow('Frame', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
video.release()
cv2.destroyAllWindows()
