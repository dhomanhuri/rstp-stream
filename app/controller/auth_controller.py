from app.model.user import User

from app import response, app, db
from flask import request, render_template, request

def login():
    email = request.form['email']
    password = request.form['password'].encode('utf8')


def register():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        users = User(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        return response.success(users,'success add user')
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
