from app import app
from app.controller import rtsp_controller

from flask import Response, render_template


@app.route('/')
def index():
    return 'hello flask'


@app.route("/html")
def index2():
    return render_template("index.html")


@app.route('/video_feed')
def video_feed():
    return Response(rtsp_controller.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
