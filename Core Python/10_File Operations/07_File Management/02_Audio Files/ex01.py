#!python3

from playsound import playsound
import os
os.system("cls")

print("\nPlaying the audio file which is in the format of \".wav\"")
print("---------------------------------------------------------", end="\n")

print("\nLoading the audio file.. Please wait..", end="\n")

playsound(r"C:\Practice\my-python-journey\DataSets\AudioFiles\beep.wav")

print("\nFinished playing the audio file.. now terminating")


"""
1. If higher version of playsound is not supported then 
    1. Uninstall playsound if already installed
        pip uninstall playsound
    2. Install playsound
        pip install playsound==1.2.2
"""