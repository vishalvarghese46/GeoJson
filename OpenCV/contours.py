import numpy as np
import cv2

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\shapes.jpg', 1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(grey_img, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(f'Number of contours = {str(len(contours))}')

print(f'First contour: {contours[1]}')

cv2.drawContours(img, contours, -1, (0, 255, 0), 3) #-1 argument will show all contours | specifing the right index gives the corresponding contours
cv2.imshow("dhe",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
