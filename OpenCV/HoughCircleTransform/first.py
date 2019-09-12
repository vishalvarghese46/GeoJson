import cv2
import numpy as np
import time

start = int(round(time.time() * 1000))
img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\shapes.jpg', 1)
image = cv2.medianBlur(img, 5)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(grayImage, cv2.HOUGH_GRADIENT, 1, 120,
              param1=50,
              param2=30,
              minRadius=0,
              maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

end = int(round(time.time() * 1000))
print(f'Time in Millisec: {end-start}')
print(f'Time in Sec: {(end-start)/1000}')

cv2.imshow("Dude", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

