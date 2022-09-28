import cv2
import matplotlib.pyplot as plt


def global_threshold(image, thresh, high_val, low_val):
    img = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > thresh:
                img[i, j] = high_val
            else:
                img[i, j] = low_val
    return img


ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week14//images//shape.PNG", 0)

plt.hist(ogImg.ravel(), 256, [0, 256])
plt.show()

output = global_threshold(ogImg, 225, 0, 255)

cv2.imshow("output", output)
cv2.imshow("OG", ogImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
