import cv2
import numpy

img = cv2.imread("D:\\workspace\\python\\week7\\img\\animal1.jpg")

h, w = img.shape[:2]
# print("Width: ", w, ",Height: ", h)
# rotation matrix
M = cv2.getRotationMatrix2D((w/2, h/2), 180, 3)
res = cv2.warpAffine(img, M, (w, h))

cv2.imshow("wow zaa OG!!!", img)
cv2.imshow("wow zaa RES!!!", res)
cv2.imwrite("D:\\workspace\\python\\week7\\img\\rotation.jpg", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
