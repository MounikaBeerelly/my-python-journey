#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image03.jpg")

imageEdges = cv2.Canny(loadedImage, 100, 100)

cv2.imshow("Image with Edges", imageEdges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\imageWithEdges.jpg", imageEdges)