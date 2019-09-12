import cv2
import numpy as np

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\lines.jpg', 1)

grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cannyEdge = cv2.Canny(grayImage,100,200,apertureSize = 3)
minLineLength = 30
maxLineGap = 10

lines = cv2.HoughLinesP(cannyEdge,1,np.pi/180,15,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('hough',img)
cv2.waitKey(0)