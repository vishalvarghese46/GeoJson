import cv2
import numpy as np
img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\coins.jpg', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circle = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 120, param1=50,
                                                param2=30, minRadius=0, maxRadius=0)
circle = np.uint16(np.around(circle))
for i in circle[0,:]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("Dude", cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

