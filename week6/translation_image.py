import cv2
import numpy

img = cv2.imread("D:\\workspace\\python\\week6\\img\\short.jpg")

# translation matrix
# [x], [y]
M = numpy.float32([[1, 0, -200], [0, 1, -200]])
h, w = img.shape[:2]

translate = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Original", translate)
cv2.waitKey(0)
cv2.destroyAllWindows()
