from app.model.camera import Camera

from app import response, app, db
from flask import request, render_template
import os


def index():
    try:
        return render_template("config.html", menu='none', submenu='all')

    except Exception as e:
        print(e)


def config_cam(i):
    try:
        # name = request.form.get('name')
        ip = request.form.get('ip')
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        user = Camera.query.filter_by(id=i).first()
        user.username = username
        print("after uname")
        user.ip = ip
        user.name = name
        user.password = password

        db.session.commit()
        print("after model")

        return render_template("config.html", account_cam1=f'akun berhasil di ganti dengan ip {ip} dan password {password}', cam_id=i)
        # return response.success('data', 'success add user')
    except Exception as e:
        print(e)
