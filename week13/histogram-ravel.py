import cv2
import matplotlib.pyplot as plt

# img = cv2.imread("D:/workspace/python/week13/image/rgbyGradient.jpg", 1)
img = cv2.imread("R:/workspace/image-processing-python-POEY/week13/image/shape.PNG", 1)

b, g, r = cv2.split(img)

cv2.imshow("OG", img)
plt.hist(b.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
