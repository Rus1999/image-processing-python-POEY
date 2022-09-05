import cv2

img1 = cv2.imread("D://workspace//python//week11//pic-20220905//square.jpg")
img2 = cv2.imread("D://workspace//python//week11//pic-20220905//circle.jpg")

result = cv2.subtract(img1, img2)

cv2.imshow("Output", result)
cv2.waitKey(0)
cv2.destroyAllWindows()