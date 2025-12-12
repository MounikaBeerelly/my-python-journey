#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image03.jpg", cv2.IMREAD_GRAYSCALE)

blurredImage = cv2.blur(loadedImage, (5,5))
gaussianBlurredImage = cv2.GaussianBlur(loadedImage, (5,5), 0)
medianBlurredImage = cv2.medianBlur(loadedImage, 5)

cv2.imshow("Original Image", loadedImage)
cv2.imshow("Blurred Image", blurredImage)
cv2.imshow("Gaussian Blurred Image", gaussianBlurredImage)
cv2.imshow("Median Blurred Image", medianBlurredImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\blurredImage.jpg", blurredImage)
cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\gaussianBlurredImage.jpg", gaussianBlurredImage)
cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\medianBlurredImage.jpg", medianBlurredImage)