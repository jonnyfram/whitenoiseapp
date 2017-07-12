from flask import Flask, render_template
from os import environ
import functools

app=Flask(__name__)

@app.route("/")
def main_page():
    
    return render_template('sounds.html', sound_name="sound_")
    
@app.route("/timer")
def timer():
    return render_template('timer.html')
    
@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/test")
def test():
    return render_template('test.html', sound_name="sound_name")
    
if __name__ == "__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))
    


