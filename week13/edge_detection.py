import cv2

img = cv2.imread("R:/workspace/image-processing-python-POEY/week13/image/rose.jpg", 1)

edgeFalse = cv2.Canny(img, 77, 350)
# edgeTrue = cv2.Canny(img, 50, 150, True)

cv2.imshow("OG", img)
# cv2.imshow("WOW ZAA!!!", edgeTrue)
cv2.imshow("WOW ZAA!!!!", edgeFalse)
cv2.imwrite("R:/workspace/image-processing-python-POEY/week13/image/rose-edge.jpg", edgeFalse)

cv2.waitKey(0)
cv2.destroyAllWindows()
