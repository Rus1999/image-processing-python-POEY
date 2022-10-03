import cv2
import matplotlib.pyplot as plt

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week14//images//text.jpg", 0)

# histogram
# plt.hist(ogImg.ravel(), 256, [0, 254])
# plt.show()

# cv2.threshold(src, thresh, maxval, type)

# THRESH_BINARY
# dst(x,y) =    {maxval if src(x,y) > thresh
#               {0      otherwise
# ret, thresh_binary = cv2.threshold(ogImg, 200, 255, cv2.THRESH_BINARY)
# cv2.imshow("output", thresh_binary)

# THRESH_BINARY_INV
# dst(x,y) =    {0      if src(x,y) > thresh
#               {maxval otherwise
# ret, thresh_binary_inv = cv2.threshold(ogImg, 200, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("output", thresh_binary_inv)

# THRESH_TRUNC
# dst(x,y) =    {threshold  if src(x,y) > thresh
#               {src(x,y)   otherwise
# ret, thresh_trunc = cv2.threshold(ogImg, 200, 0, cv2.THRESH_TRUNC)
# cv2.imshow("output", thresh_trunc)

# THRESH_TOZERO
# dst(x,y) =    {src(x,y)   if src(x,y) > thresh
#               {0          otherwise
ret, thresh_tozero = cv2.threshold(ogImg, 200, 0, cv2.THRESH_TOZERO)
cv2.imshow("output", thresh_tozero)

# THRESH_TOZERO_INV
# dst(x,y) =    {0             if src(x,y) > thresh
#               {src(x,y)      otherwise
# ret, thresh_tozero_inv = cv2.threshold(ogImg, 200, 0, cv2.THRESH_TOZERO_INV)
# cv2.imshow("output", thresh_tozero_inv)

# computer vision(0-20), image processing(130-180), background(230-250)
cv2.imwrite("R://workspace//image-processing-python-POEY//week14//images//text_result.jpg", thresh_tozero)
cv2.imshow("OG", ogImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
