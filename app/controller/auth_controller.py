from app.model.user import User
from app.model.camera import Camera

from app import response, app, db
from flask import request, render_template, request, flash, redirect, url_for


def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()

    if not user:
        flash("Email not registed")
        return redirect(url_for('login'))

    if not user.checkPassword(password):
        flash("Password Salah")
        return redirect(url_for('login'))

    cameras = Camera.query.all()
    data = serialize_cameras(cameras)
    return render_template("index.html", menu='none', submenu='none',)


def logout():
    return redirect(url_for('login'))


def register():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        users = User(name=name, email=email)
        users.setPassword(password)
        data = serialize_data(users)
        db.session.add(users)
        db.session.commit()
        return response.success(data, 'success add user')
    except Exception as e:
        print(e)


def update_account():
    try:
        # name = request.form.get('name')
        email = request.form.get('email')
        password_nosalt = request.form.get('password')

        user = User.query.filter_by(id=1).first()

        user.email = email
        # user.password = password_nosalt

        user.setPassword(password_nosalt)

        db.session.commit()
        return render_template("config.html", account=f'akun berhasil di ganti dengan email {email} dan password {password_nosalt}', cam1='', cam2='', cam3='')
        # return response.success('data', 'success add user')
    except Exception as e:
        print(e)


def serialize_data(user):
    return {
        'name': user.name,
        'email': user.email,
        'password': user.password,
    }


def serialize_cameras(cameras):
    return [
        {
            'id': camera.id,
            'name': camera.name,
            'ip': camera.ip,
            'created_at': camera.created_at,
            'updated_at': camera.updated_at
        }
        for camera in cameras
    ]
