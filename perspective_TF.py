import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.png')
row, col, ch = img.shape

pt1 = np.float32([[0,0], [412,50], [442,443], [200,438]])
pt2 = np.float32([[0,0],[300, 0],[300,300], [0,300]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)
wraped = cv2.warpPerspective(img, matrix, (col, row))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("raw image")

plt.subplot(1,2,2)
plt.imshow(wraped)
plt.title("wraped Image")
#
#cv2.imshow('wr',wraped)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
