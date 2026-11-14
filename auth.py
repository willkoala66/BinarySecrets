import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

import rstr

class authcodes:
    authCodes = []
        
    def get_auth(self):
        return self.authCodes
    def add_auth(self, auth):
        self.authCodes.append(auth)
    

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE userid = ?', (user_id,)
        ).fetchone()


@bp.route('/register', methods=('GET', 'POST'))
def register():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute("INSERT INTO user (username, password, email, pfp_path, chats) VALUES (?, ?, ?, ?, ?)",(username, generate_password_hash(password), email, "/static/uploads/pfps/eggbert.png", "{'chats':[]}"))
                db.commit()
            except db.IntegrityError as x:
                error = f"User {username} is already registered.: {x.sqlite_errorname}"
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['userid']
            from app import authcodes as authcodes
            authcodes.add_auth(rstr.getSessionArgs(True))
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        authCodeClear = False
        from app import authcodes as authcodes
        for i in authcodes.get_auth():
            if rstr.check_string(i ,rstr.getSessionArgs(False)):
                authCodeClear = True
            else:
                authCodeClear = False
        if g.user is None and not authCodeClear:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view