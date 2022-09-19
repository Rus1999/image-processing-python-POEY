import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/workspace/python/week12/images/sea.png", 1)


hist0 = cv2.calcHist([img], [0], None, [256], [0, 256])
hist1 = cv2.calcHist([img], [1], None, [256], [0, 256])
hist2 = cv2.calcHist([img], [2], None, [256], [0, 256])

cv2.imshow("WOW ZAA!!!", img)
plt.plot(hist0)
plt.plot(hist1)
plt.plot(hist2)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
