import cv2

# ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week15//images//textbook2.jpg", 0)
ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week15//images//textbook.jpg", 0)

# adt_mean = cv2.adaptiveThreshold(ogImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 7)
adt_gaussian = cv2.adaptiveThreshold(ogImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 7)

# cv2.imshow("mean", adt_mean)
cv2.imshow("gaussian", adt_gaussian)
cv2.imshow("OG", ogImg)
cv2.imwrite("R://workspace//image-processing-python-POEY//week15//images//adt_gaussian.png", adt_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
