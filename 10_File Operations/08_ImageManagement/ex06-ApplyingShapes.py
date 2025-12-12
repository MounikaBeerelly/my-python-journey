#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image01.png")

print("\nApplying required shapes... Please wait...")

cv2.rectangle(loadedImage, (50,50), (150,150), (0,255,0), 3)
cv2.circle(loadedImage, (20,20), 10, (255,0,0), 2)
cv2.line(loadedImage, (0,0), (500,500), (0,0,255),5)

cv2.imshow("Applied Shapes", loadedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()