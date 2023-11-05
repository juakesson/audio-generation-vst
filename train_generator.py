#Training script for an audio generator built using pytorch 

#Imports
import torch
import torchaudio
import os

print(torch.__version__)
print(torchaudio.__version__)

#Import some audio data
audiodir = "/mnt/data/"

#Load the metadata of the audio files
meta_list = [] 
for audio_file in os.listdir(audiodir):
    meta_list.append(torchaudio.info(audiodir))

x = 1



