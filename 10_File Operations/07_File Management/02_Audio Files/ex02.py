#!python3

from playsound import playsound
import os
os.system("cls")

print("\nPlaying the audio file which is in the format of \".mp3\"")
print("---------------------------------------------------------", end="\n")

print("\nLoading the audio file.. Please wait..", end="\n")

playsound(r"C:\Practice\my-python-journey\DataSets\AudioFiles\tone.mp3")

print("\nFinished playing the audio file.. now terminating")


"""
Note:
-----
1. Playsound will load the audio file .mp3 file and then plays the file directly
2. Playsound utilizes the internal operating system's audio API and plays the file
"""