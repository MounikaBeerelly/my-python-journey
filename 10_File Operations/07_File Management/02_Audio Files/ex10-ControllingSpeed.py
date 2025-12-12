#!python3

import os
os.system("cls")
from pydub import AudioSegment
from pydub.playback import play

print("\nControlling the Speed of the audio file")
print("------------------------------------------", end="\n")

audioFilePath = r"C:\Practice\my-python-journey\DataSets\AudioFiles\sample.mp3"
os.environ["TMPDIR"] = r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData"

print("\nPlaying the audio file in original speed..")
audioFile = AudioSegment.from_file(audioFilePath, format = "mp3")
play(audioFile)

print("\nPlaying the audio file in increasing the speed by 2 time...")
fasterAudio = audioFile._spawn(audioFile.raw_data, overrides = {"frame_rate" : int(audioFile.frame_rate * 2)})
fasterAudio = fasterAudio.set_frame_rate(audioFile.frame_rate)
fasterAudio.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\FasterAudio.mp3", format = "mp3")
print("\nPlaying the faster audio file... Please wait...", end="\n")
play(fasterAudio)
print("\nFinished playing the audio file.. now terminating")

print("\nPlaying the audio file in decreasing the speed by 2 time...")
slowerAudio = audioFile._spawn(audioFile.raw_data, overrides = {"frame_rate" : int(audioFile.frame_rate / 2)})
slowerAudio = slowerAudio.set_frame_rate(audioFile.frame_rate)
slowerAudio.export(r"C:\Practice\my-python-journey\DataSets\AudioFiles\SoundData\SlowerAudio.mp3", format = "mp3")
print("\nPlaying the slower audio file... Please wait...", end="\n")
play(slowerAudio)
print("\nFinished playing the audio file.. now terminating")
