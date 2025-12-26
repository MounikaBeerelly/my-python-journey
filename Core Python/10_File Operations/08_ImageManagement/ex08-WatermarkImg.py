#!python3

import cv2
import os
os.system("cls")

print("\nReading the image file Please wait...", end="\n")

loadedImage = cv2.imread(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\Images\image02.jpg")

cv2.putText(loadedImage, "Hello...", (5,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow("Image with Text", loadedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Practice\my-python-journey\10_File Operations\08_ImageManagement\savedFiles\imageWithText.jpg", loadedImage)