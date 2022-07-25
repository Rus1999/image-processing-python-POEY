import cv2

img = cv2.imread("D:\\workspace\\python\\week5\\img\\harvest-moon-dog.png", 1)

# return (height, width, channel)
print(img.shape)
print(img.size)
# img[height, width] return (0, 0, 0) or 0 for grayscale
print(img[155, 422])

h, w = img.shape[:2]
print("Height: {}, Width: {}".format(h, w))

b, g, r = img[155, 422]
print("B: {}, G: {}, R: {}".format(b, g, r))

# crop [start_row:end_row, start_col:end_col]
crop_img = img[27:523, 146:664]

cv2.imshow("Result", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
