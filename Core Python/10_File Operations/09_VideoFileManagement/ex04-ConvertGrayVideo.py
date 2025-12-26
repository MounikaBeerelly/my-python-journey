#!python3

import os
os.system("cls")

import cv2

print("\nCreating an object for capturing the video..", end="\n")

captureVideo = cv2.VideoCapture(r"C:\Practice\my-python-journey\10_File Operations\09_VideoFileManagement\Videos\Video03.mp4")

if not captureVideo.isOpened() :
    print("\nFatal Error! could not open the video file..", end="\n")
    exit()

print("\nReading the video file until it is completely read...", end="\n")

windowWidth = 640
windowHeight = 480

while (captureVideo.isOpened()) :
    frameReturned, frameValue = captureVideo.read()
    
    if frameReturned == True :
        resizedFrame = cv2.resize(frameValue, (windowWidth, windowHeight))
        
        grayFrame = cv2.cvtColor(resizedFrame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Resized window Frame : ", grayFrame)
        
        if cv2. waitKey(25) & 0xFF == ord('q') :
            break
    else :
        break
    
captureVideo.release()
cv2.destroyAllWindows()
