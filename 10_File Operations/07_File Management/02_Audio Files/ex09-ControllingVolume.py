#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nControlling the volume of the audio file")
print("------------------------------------------", end="\n")

audioFilePath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"

audioFile = AudioSegment.from_file(audioFilePath, format = "mp3")

volumeChoice = input("\nDo you want to control the volume of the audio file (Y: Yes, N:No) :")

if(volumeChoice == "Y") :
    volumeControlChoice = input("\nPlease enter the volume control type (I: Increase, D: Decrease) : ")
    if volumeControlChoice == "I" :
        louderAudio = audioFile + 6
        louderAudio.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\IncreaseVolumne.mp3", format = "mp3")
        os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"
        print("\nPlaying the audio file Louder by 6DB... Please wait...", end="\n")
        play(louderAudio) # specify the temporary file path
        print("\nFinished playing the audio file.. now terminating")
    else :
        quiterAudio = audioFile - 6
        quiterAudio.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\DecreaseVolumne.mp3", format = "mp3")
        os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"
        print("\nPlaying the audio file Quiter by 6DB... Please wait...", end="\n")
        play(quiterAudio) # specify the temporary file path
        print("\nFinished playing the audio file.. now terminating")

    