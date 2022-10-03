import cv2
import matplotlib.pyplot as plt


def global_threshold(image, thresh_max1, thresh_min1, thresh_max2, thresh_min2, high_val, low_val):
    img = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if thresh_max1 > image[i, j] > thresh_min1 or thresh_max2 > image[i, j] > thresh_min2:
                img[i, j] = high_val
            else:
                img[i, j] = low_val
    return img


ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week14//images//shape.PNG", 0)

# plt.hist(ogImg.ravel(), 256, [0, 256])
# plt.show()

# b, g, r = cv2.split(ogImg)

# # star(blue)
# b_remove = global_threshold(b, 100, 255, 0)
#
# # triangle(green)
# g_remove = global_threshold(g, 100, 255, 0)
#
# # square(red)
# r_remove = global_threshold(r, 100, 255, 0)
#
# # hexagon(yellow)

# plt.hist(ogImg.ravel(), 256, [0, 256])
# plt.show()

# star(90) square(145) triangle(200) hexagon(240) bg(255)
# star(between 80-100) hexagon(between 240.9-241.5)
# star_rectangle = global_threshold(ogImg, 150, 80, 255, 0)
# rectangle = global_threshold(ogImg, 150, 140, 255, 0)
# img_result = cv2.addWeighted(star, 1, rectangle, 1, -35)
all = global_threshold(ogImg, 241, 80, 241.5, 240.9, 255, 0)

cv2.imwrite("R://workspace//image-processing-python-POEY//week15//images//all.PNG", all)
cv2.imshow("output", all)
cv2.imshow("OG", ogImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
