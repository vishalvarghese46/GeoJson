import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'E:\Python\OpenCVLearning\OpenCV\images\dude.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, threshold1=100, threshold2=200)
titles = ['image', 'canny']
images = [gray, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()