import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, abort
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.model import User
from flaskr.db import session_scope

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if os.environ['FLASK_ENV'] == 'production':
            error = "Sorry, registration is now closed."
        elif not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first() is not None:
            error = 'Username {} is already registered.'.format(username)

        if error is None:
            user = User(username=username,
                        password=generate_password_hash(password))
            with session_scope() as sess:
                sess.add(user)
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        user = User.query.get(user_id)
        g.user = user


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/signin', methods=('POST',))
def signin():
    username = request.json['username']
    password = request.json['password']
    error = None
    user = User.query.filter_by(username=username).first()

    if user is None:
        error = 'Incorrect'
    elif not check_password_hash(user.password, password):
        error = 'Incorrect'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return jsonify({
            'status': 'success' 
        })
    else:
        return abort(401, {'message': error})

@bp.route('/signout', methods=('POST',))
def signout():
    session.clear()
    return jsonify({
        'status': 'success'
    })


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
