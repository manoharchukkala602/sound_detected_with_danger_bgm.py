import sounddevice as pd
from pathlib import Path
import simpleaudio as sa
alert =sa.WaveObject.from_wave_file("/Users/manoharchukkala/Downloads/danger_real.wav") 

import numpy as np
import pyttsx3 as pt
import os

engine =pt.init()
engine.say("hi i am your monitar......")
engine.runAndWait()
thresold =0.01
def audio_call(indata,frame,time,status):
    varma = np.linalg.norm(indata)/len(indata)
    
    if varma>thresold:
      engine.say("sound detected...........")
      alert.play()
        
      print("detected")
with pd.InputStream(callback=audio_call):
    print("listening")
    while True:
         pass

         

    