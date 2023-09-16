# from app.model.camera import Camera

from app import response, app, db
from flask import request, render_template
import os


def index():
    try:
        image_folder = 'app/static/human'
        images = [f for f in os.listdir(image_folder) if f.endswith(
            ('.jpg', '.png', '.jpeg', '.gif'))]
        
        return render_template("all-galery.html", menu='none', submenu='all', data=images)

    except Exception as e:
        print(e)
