#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image01.png")

print("\nRotating the image.. Please wait...")

(imgHeight, imgWidth) = loadedImage.shape[:2]

imageCenter = (imgWidth/2, imgHeight/2)
rotateMatrix = cv2.getRotationMatrix2D(imageCenter, 45, 1.0)
finalRotatedImage = cv2.warpAffine(loadedImage, rotateMatrix, (imgWidth, imgHeight))

print("\nDisplaying the image..Please wait...", end="\n")
cv2.imshow("Rotated Image", finalRotatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()