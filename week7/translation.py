import cv2
import numpy

img = cv2.imread("D:\\workspace\\python\\week7\\img\\animal1.jpg")

# translation image
M = numpy.float32([[1, 0, -405], [0, 1, -435]])
h, w = img.shape[:2]

translation = cv2.warpAffine(img, M, (w, h))

cv2.imshow("wow zaa !!", translation)
cv2.imwrite("D:\\workspace\\python\\week7\\img\\translation1.jpg", translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
