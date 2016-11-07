import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera, VideoCameraWithBox
import time
import os, sys, string
from flask_login import LoginManager, UserMixin
from contextlib import closing
from werkzeug.debug import DebuggedApplication
#from flask_socketio import SocketIO


app = Flask(__name__)
#socketio = SocketIO(app)
names = ["Rebecca K.", "Doug C.", "Charles N.", "John D."]
colors = ["green", "red", "blue", "yellow"]
icons = ["user", "warning-sign", "comment-alt", "envelope"]

@app.route('/')
def index():
    return render_template('index.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/messages')
def messages():
    starglyphs = ["star", "dislikes"]
    papglyphs = ["paperclip", ""]
    labels = ["warning", "success", "info", ""]
    names = ["Rebecca K.", "Doug C.", "Charles N.", "John D."]
    return render_template('messages.html', user = "Rebecca Krauthamer", starglyphs = starglyphs, papglyphs = papglyphs, labels = labels, names = names, colors = colors, icons = icons)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/chart')
def chart():
    return render_template('chart.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/login')
def login():
    return render_template('login.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/icon')
def icon():
    return render_template('icon.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/form')
def form():
    return render_template('form.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/cameras')
def cameras():
    return render_template('gallery.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', user = "Rebecca Krauthamer", names = names, colors = colors, icons = icons)

def gen(camera):
    print "gen"
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video1_feed')
def video1_feed():
    c = gen(VideoCameraWithBox())
    return Response(c, mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2_feed')
def video2_feed():
    c = gen(VideoCamera())
    return Response(c, mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
    #socketio.run(app)
