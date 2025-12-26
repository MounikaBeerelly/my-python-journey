#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nCombining the audio files to one single file")
print("---------------------------------------------------------", end="\n")

audioPath01 = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"
audioPath02 = r"C:\Practice\my-python-journey\DataSets\AudioFiles\tone.mp3"

audioFile01 = AudioSegment.from_mp3(audioPath01)
audioFile02 = AudioSegment.from_mp3(audioPath02)

print("\nCombining the audio files.. Please wait..", end="\n")

combineFile = audioFile01 + audioFile02

print("\nExporting the combined audio file...", end="\n")

combineFile.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\combineFile.mp3", format = "mp3")

print("\nHey! Combining and Exporting the audio file is successful")

combinedFilePath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\combineFile.mp3"
loadMusicFile = AudioSegment.from_mp3(combinedFilePath)
os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"

print("\nPlaying the audio files.. please wait..", end="\n")
play(loadMusicFile) # specify the temporary file path
print("\nFinished playing the audio file.. now terminating")

