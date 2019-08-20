import cv2
import numpy as np

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\david.jpg', 1)

cv2.line(img, (0, 1000), (150, 150), (255,255, 255), 15) #point1, point2 and then there is the BGR color combo followed by the line width
cv2.rectangle(img, (15, 25), (163, 259), (0,255,0), 15)
cv2.circle(img, (725, 490), 55, (0, 0, 255), -1)

points = np.array([[120,125], [204, 301], [702, 230], [503,101]], np.int32)
cv2.polylines(img, [points], True, (255,0,0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "David Beckham", (250,350), font, 1, (200, 255,255), 2, cv2.LINE_AA)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
