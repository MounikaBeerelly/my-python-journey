#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\Python Libraries.jpg")

print("\nDisplaying the image... Please wait...")
cv2.imshow("Loaded Image", loadedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()