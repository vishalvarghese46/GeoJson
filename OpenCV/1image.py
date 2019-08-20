import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\dude.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

cv2.imshow('image', img)
cv2.imshow('gray', gray)

cv2.waitKey(0) #waits for any key to be pressed
cv2.destroyAllWindows()