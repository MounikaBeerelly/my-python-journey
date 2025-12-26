#!python3

import os
os.system("cls")

import cv2

print("\nCreating an object for capturing the video..", end="\n")

captureVideo = cv2.VideoCapture(r"C:\Practice\my-python-journey\10_File Operations\09_VideoFileManagement\Videos\Video02.mp4")

if not captureVideo.isOpened() :
    print("\nFatal Error! could not open the video file..", end="\n")
    exit()
    
frameWidth = int(captureVideo.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(captureVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("\nThe width of the captured video is : ", frameWidth, end="\n")
print("\nThe height of the captured video is : ", frameHeight, end="\n")

fpsVideo = captureVideo.get(cv2.CAP_PROP_FPS)

print("\nThe frames per second of the captured video is : ", fpsVideo, end="\n")

captureVideo.release()

"""
Output:
-------
Creating an object for capturing the video..

The width of the captured video is :  1920

The height of the captured video is :  1080

The frames per second of the captured video is :  29.97002997002997
"""