#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage01 = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image02.jpg")
loadedImage02 = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image04.jpg")

loadedImage02 = cv2.resize(loadedImage02, (loadedImage01.shape[1], loadedImage01.shape[0]))

alphaValue = 0.40
betaValue = 1 - alphaValue

blendImage = cv2.addWeighted(loadedImage01, alphaValue, loadedImage02, betaValue, 0)

cv2.imshow("Blended Shapes", blendImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\blendImage.jpg", blendImage)