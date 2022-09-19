import cv2

img = cv2.imread("D:/workspace/python/week13/image/campfire.jpg")

blur = cv2.GaussianBlur(img, (7, 7), 8)
sharp = cv2.addWeighted(img, 2, blur, -1, 0)

cv2.imshow("OG", img)
# cv2.imshow("Blur", blur)
cv2.imshow("WOW ZAA!!!", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
