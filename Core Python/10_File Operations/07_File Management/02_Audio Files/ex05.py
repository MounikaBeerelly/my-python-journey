#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nPlaying the audio file is in the format of \".mp3\"")
print("---------------------------------------------------------", end="\n")

audioPath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"

print("\nLoading the audio file.. Please wait..", end="\n")

loadMusicFile = AudioSegment.from_file(file = audioPath, format = "mp3")
os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"

print("\nPlaying the audio files.. please wait..", end="\n")
play(loadMusicFile) # specify the temporary file path

print("\nFinished playing the audio file.. now terminating")

