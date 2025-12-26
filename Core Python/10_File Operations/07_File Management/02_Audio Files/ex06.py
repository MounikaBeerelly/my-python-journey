#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nPlaying the audio file is in the format of \".mp3\"")
print("---------------------------------------------------------", end="\n")

audioPath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"

print("\nLoading the audio file.. Please wait..", end="\n")

loadMusicFile = AudioSegment.from_mp3(file = audioPath)

print("\nExporting the audio file from MP3 format to WAV format..", end="\n")
loadMusicFile.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\test.wav", format = "wav")

print("\nHey! exporting the audio file from MP3 to WAV format is successful")

print("\nFinished playing the audio file.. now terminating")

