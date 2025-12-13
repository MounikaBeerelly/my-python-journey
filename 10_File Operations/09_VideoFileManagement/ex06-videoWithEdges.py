#!python3

import os
os.system("cls")

import cv2

print("\nCreating an object for capturing the video..", end="\n")

captureVideo = cv2.VideoCapture(r"C:\Practice\my-python-journey\10_File Operations\09_VideoFileManagement\Videos\Video04.mp4")

if not captureVideo.isOpened() :
    print("\nFatal Error! could not open the video file..", end="\n")
    exit()

print("\nReading the video file until it is completely read...", end="\n")

windowWidth = 640
windowHeight = 480

videoFourCC = cv2.VideoWriter_fourcc(*'mp4v') # code that should be used for mp4 videos
outvideoFile = cv2.VideoWriter(r"C:\Practice\my-python-journey\10_File Operations\09_VideoFileManagement\savedVideos\videoWithEdges.mp4", videoFourCC, 20.0, (windowWidth, windowHeight))

while (captureVideo.isOpened()) :
    frameReturned, frameValue = captureVideo.read()
    
    if frameReturned == True :
        
        resizedFrame = cv2.resize(frameValue, (windowWidth, windowHeight))
        grayFramevideo = cv2.cvtColor(resizedFrame, cv2.COLOR_BGR2GRAY)
        
        videoEdges = cv2.Canny(grayFramevideo, 100, 200)

        outvideoFile.write(resizedFrame)
        cv2.imshow("Current Frame : ", videoEdges)
        
        if cv2. waitKey(25) & 0xFF == ord('q') :
            break
    else :
        break
    
    
captureVideo.release()
outvideoFile.release()
cv2.destroyAllWindows()
