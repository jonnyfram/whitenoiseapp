from flask import Flask, render_template, request
from os import environ
import functools
from pydub import AudioSegment
from pydub.playback import play
import wave

import time
import sounds

app=Flask(__name__)

@app.route("/")
def main_page():
    print("GONNA TRY AND PLAY THE SOUND")
    #song = AudioSegment.from_wav("home/ubuntu/workspace/audio/test.wav")
    #play(song)
    
    wave.open('home/ubuntu/workspace/audio/test.wav', mode='r')

    return render_template('sounds.html', sound_name="sound_")
    
@app.route("/timer", methods=["GET", "POST"])
def timer():
    #testing button passing int
    #q_timer=request.form["test"]
    #print(q_timer)
    
    
    #Quick timer
    
    timer_len = int(request.args.get('timer_len', 0))
    if timer_len < 1:
        timer_len = 0
    if timer_len == 0:
        timer_len = 0
    else:
        timer_len = int(request.args.get('timer_len', 0))
        
    if timer_len > 1440*60:
        timer_len = 1440
        print("Timer capped at 1 day continuous play!")
    
    print("Timer length "+str(timer_len)+" mins")
    sounds.set_timer(timer_len)
    
    
    return render_template('timer.html')
    
@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/test")
def test():
    return render_template('test.html', sound_name="sound_name")
    
if __name__ == "__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))
    


