from flask import Flask, render_template, request
from os import environ
import functools
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

import time
from threading import Timer

def playsound():
    """Play sounds passed from user interface"""
    pass

def stop_sound():
    """Stop all sounds"""
    print("Timer completed at "+ str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    #stop sound/s

def set_timer(timer_len):
    """Set the timer based on user input"""
    mins=0
    
    # after timer_len completed call a function. dummy function above 
    # convert our timer_len to minutes (timer works in seconds)
    timer_len = timer_len*60
    t = Timer(timer_len, stop_sound)
    t.start()
    
    #while timer_len != mins:
        #print ">>>>>>>>>>>>>>>>>>>>>", mins
        # Sleep for a minute
        #time.sleep(1)
        # Increment the minute total
        #print(str(timer()))
        #mins += 1

def fade():
    pass
    #if fade is required play the sound with modifications (see pydub doc on how to do this effectively)