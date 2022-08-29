import cv2
import numpy

img1 = cv2.imread("D://workspace//python//week9//images//gokublack.jpg")
img2 = cv2.imread("D://workspace//python//week9//images//lightning.png")

# image1, image1_weight, image2, image2_weight, gammaValue
img_result = cv2.addWeighted(img1, 0.5, img2, 1, -35)

cv2.imshow("WOW ZAA!!!", img_result)
cv2.imwrite("D://workspace//python//week9//images//gokublacknlightning.jpg", img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
