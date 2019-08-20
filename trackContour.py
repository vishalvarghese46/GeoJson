import numpy as np
import cv2

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\track.jpg')

#crop_img = frame[60:120, 0:160] | Croppeing the bottom half of the image

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray_img, (5, 5), 0) #Gaussian blur

ret, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV) #Color thresholding

contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

if len(contours) > 0:
    c = max(contours, key=cv2.contourArea)
    M = cv2.moments(c)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.line(img, (cx,0), (cx,720), (255,0,0), 1)
    cv2.line(img, (0,cy), (1280,cy), (255,0,0), 1)

    cv2.drawContours(img, contours, -1, (0,255,0), 1)
else:
    print("Can't see shit dawg!")

print(cx)
print(cy)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

