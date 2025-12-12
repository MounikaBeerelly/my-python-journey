#!python3

from playsound import playsound
import os
os.system("cls")

def playaudioFiles(inChoice) :
    audioFiles = {
        "1" : r"C:\Practice\my-python-journey\DataSets\AudioFiles\tone.mp3",
        "2" : r"C:\Practice\my-python-journey\DataSets\AudioFiles\beep.wav",
        "3" : r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.wav",
        "4" : r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"
    }
    
    if (inChoice in audioFiles) :
        print(f"Playing {audioFiles[inChoice]}..", end="\n")
        playsound(audioFiles[inChoice])
    else :
        print("Hey! Invalid choice..", end="\n")

print("\nPlaying the audio file as per the given choice")
print("---------------------------------------------------------", end="\n")

inAudioChoice = input("\nPlease enter your choice to play the sound (1/2/3/4) : ")

print("\nPlaying the audio file.. Please wait..", end="\n")

playaudioFiles(inAudioChoice)

print("\nFinished playing the audio file.. now terminating")

