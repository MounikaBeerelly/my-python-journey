#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image03.jpg", cv2.IMREAD_GRAYSCALE)

_, binaryImage = cv2.threshold(loadedImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", binaryImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\thresholdImage.jpg", binaryImage)