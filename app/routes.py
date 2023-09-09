from app import app
from app.controller import rtsp_controller, camera_controller, camera1_controller

from flask import Response, render_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/cam1')
def cam1():
    return camera1_controller.index()
    # return render_template("cam1.html", menu='master', submenu='cam1')


@app.route('/cam2')
def cam2():
    return render_template("cam2.html", menu='master', submenu='cam2')


@app.route('/cam3')
def cam3():
    return render_template("cam3.html", menu='master', submenu='cam3')


@app.route('/all', methods=['GET'])
def allroute():
    return camera_controller.index()


@app.route("/cctv")
def index2():
    return render_template("index.html")


@app.route('/video_feed/<string:ip>')
def video_feed(ip):
    return Response(rtsp_controller.gen_frames(ip), mimetype='multipart/x-mixed-replace; boundary=frame')
