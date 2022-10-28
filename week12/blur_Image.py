import cv2

img = cv2.imread("R://workspace//image-processing-python-POEY//week12//images//noise.png")

# averaging blur
avg_blur = cv2.blur(img, (7, 7))

# box filter
box_filter = cv2.boxFilter(img, -1, (7, 7), normalize=True)

# gaussian blur
gaussian_blur = cv2.GaussianBlur(img, (7, 7), 0)

# median filter
median_filter = cv2.medianBlur(img, 7)

# bilateral filter
bilateral_filter = cv2.bilateralFilter(img, 21, 49, 154)
# bilateral_filter2 = cv2.bilateralFilter(img, 7, 0, 100)
# bilateral_filter3 = cv2.bilateralFilter(img, 7, 75, 75)

cv2.imshow("OG", img)
# cv2.imshow("AVG",g avg_blur)
# cv2.imshow("BoxFilter", box_filter)
# cv2.imshow("Gaussian blur", gaussian_blur)
# cv2.imshow("Median filter", median_filter)
cv2.imshow("Bilateral filter", bilateral_filter)
# cv2.imshow("Bilateral filter2", bilateral_filter2)
# cv2.imshow("Bilateral filter3", bilateral_filter3)

cv2.imwrite("R://workspace//image-processing-python-POEY//week12//images//noise_after.png", bilateral_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
