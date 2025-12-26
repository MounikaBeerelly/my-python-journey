#!python3

import os
os.system("cls")

import cv2

print("\nCreating an object for capturing the video..", end="\n")

captureVideo = cv2.VideoCapture(r"C:\Practice\my-python-journey\10_File Operations\09_VideoFileManagement\Videos\Video02.mp4")

if not captureVideo.isOpened() :
    print("\nFatal Error! could not open the video file..", end="\n")
    exit()

while (captureVideo.isOpened()) :
    frameReturned, frameValue = captureVideo.read()
    
    if frameReturned == True :
        cv2.imshow("Current Frame : ", frameValue)
        
        if cv2. waitKey(25) & 0xFF == ord('q') :
            break
    else :
        break
    
captureVideo.release()
cv2.destroyAllWindows()
