import flask
from flask import session, url_for, flash
import auth
import rstr
import os
from werkzeug.utils import secure_filename

from db import get_db

from werkzeug.security import check_password_hash

bp = flask.Blueprint("webapp", __name__, url_prefix="/app")

UPLOAD_FOLDER_PFP=os.path.join('', 'uploads/pfps')
ALLOWED_EXTENSIONS={ 'png', 'jpg', 'jpeg', 'webp', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
           
           
def file_upload(currentUrl, returnUrl, UPLOAD_FOLDER):
     if flask.request.method == 'POST':
            url = flask.url_for(currentUrl)
            # check if the post request has the file part
            if 'file' not in flask.request.files:
                flask.flash('No file part')
                return flask.redirect(url)
            file = flask.request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flask. flash('No selected file')
                return flask.redirect(url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.path.join("./static/",UPLOAD_FOLDER), filename))
                db = get_db()
                error = "Done"
                # db.execute(f"INSERT INTO user(pfp_path) WHERE userid == ({flask.session["user_id"]}) VALUES ({os.path.join(UPLOAD_FOLDER, filename)})") # DO NOT USE
                try:
                    db.execute(f"UPDATE user SET pfp_path = ('{os.path.join(UPLOAD_FOLDER, filename)}') WHERE userid = ('{flask.session["user_id"]}') ")
                    db.commit()
                except:
                    error = "It NO WORK For DB"
                flash(error)
                return flask.redirect(flask.url_for(returnUrl))



@bp.route("/profile")
@auth.login_required
def profile_page():
    authCode= str(rstr.getSessionArgs(False))
    userid = session['user_id']
    db = get_db()
    userinfo = db.execute(f"SELECT * FROM user WHERE userid = {userid}").fetchall()
    username = userinfo[0]['username']
    email = userinfo[0]['email']
    pfp_path = url_for('static',filename=userinfo[0]['pfp_path'])
    return flask.render_template("app/profile.html", authCode=authCode, userid=userid, username=username, email=email, pfp_href=pfp_path)
    
@bp.route("/profile/pfpchange", methods=["GET", "POST"])
@auth.login_required
def pfpchange():
    file_upload('webapp.pfpchange', 'webapp.profile', UPLOAD_FOLDER_PFP)
    return flask.render_template("app/uploading/pfp-upload.html")





##############################################
#                                            #
#         MAIN FUNCTION FOR webapp()         #
#                                            #
#                                            #
##############################################


@bp.route('/')
@auth.login_required
def webappmain():
    userid = session['user_id']
    db = get_db()
    userinfo = db.execute(f"SELECT * FROM user WHERE userid = {userid}").fetchall()
    chats = userinfo[0]['chats']
    
    
    
    return flask.render_template('app/main.html')
