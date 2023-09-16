from app.model.camera import Camera

from app import response, app, db
from flask import request, render_template


def index():
    try:
        cameras = Camera.query.get(1)
        data = serialize_cameras(cameras)
        return render_template("cam1.html", menu='master', submenu='cam1', data=data)

    except Exception as e:
        print(e)


def serialize_cameras(camera):
    return {
        'id': camera.id,
        'name': camera.name,
        'ip': camera.ip,
        'created_at': camera.created_at,
        'updated_at': camera.updated_at
    }
