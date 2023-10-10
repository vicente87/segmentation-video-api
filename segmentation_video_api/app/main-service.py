"""Segmentation API module."""

from moviepy.editor import *
import time
import sys

#upload video from bucket

video = VideoFileClip(sys.argv[1])


duration = video.duration

# poner esto como una variable de entrada en la creacion del servicio OJOOO

time_seg=5

for n in range(time_seg,int(duration),time_seg):
    name_a=""
    name_f=""
    
    clip_1=video.subclip(n-time_seg,n)
    audio = clip_1.audio
    name_a=str(sys.argv[2])+"_"+str(n)+".mp3"
    audio.write_audiofile(name_a)
    name_f=str(sys.argv[2])+"_"+str(n)+".png"
    video.save_frame(name_f, t=n) 
    time.sleep(1)



