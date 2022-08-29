import cv2
import numpy

img = cv2.imread('D://workspace//python//week9//images//rgb.PNG')
B, G, R = cv2.split(img)

cv2.imshow("WOW ZAA OG!!!", img)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
