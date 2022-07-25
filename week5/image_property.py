import cv2

img = cv2.imread("D:\\workspace\\python\\week5\\img\\harvest-moon-dog.png", 0)

# return (height, width, channel)
print(img.shape)
print(img.size)
# img[height, width] return (0, 0, 0) or 0 for grayscale
print(img[155, 422])

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
