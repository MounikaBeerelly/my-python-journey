#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nsplitting the audio files by specific length")
print("----------------------------------------------", end="\n")

audioFilePath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"

audioFile = AudioSegment.from_file(audioFilePath, format = "mp3")

audioLength = len(audioFile)

print("\nThe total length of the audio file : %0.2f Milliseconds, converted to minutes : %0.2f Minutes and Seconds" %(audioLength, ((audioLength/1000)/60)), end = "\n")
print("\nDefining the split point for the audio file...", end="\n")

splitPoint = audioLength/2

audioSplit01 = audioFile[: splitPoint]
audioSplit02 = audioFile[splitPoint :]

print("\nExporting the audio files that are split..", end="\n")

audioSplit01.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\split01.mp3", format = "mp3")
audioSplit02.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\split02.mp3", format = "mp3")

playChoice = input("\nDo you want to play the Audio file (Y: Yes, N:No) : ")

if(playChoice == "Y") :
    inputChoice = int(input("\nPlease enter the split number (1,2) : "))
    if inputChoice == 1 :
        loadSplitFile01 = AudioSegment.from_file(file = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\split01.mp3", format = "mp3")
        os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"
        print("\nPlaying the audio file split 01... please wait..", end="\n")
        play(loadSplitFile01) # specify the temporary file path
        print("\nFinished playing the audio file.. now terminating")
    else :
        loadSplitFile02 = AudioSegment.from_file(file = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\split02.mp3", format = "mp3")
        os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"
        print("\nPlaying the audio file split 02... please wait..", end="\n")
        play(loadSplitFile02) # specify the temporary file path
        print("\nFinished playing the audio file.. now terminating")

    