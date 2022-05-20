from flask import *
from flask_login import login_user, current_user
from ..extension import db
from ..models import Admin

login = Blueprint("login", __name__)


@login.route("/")
def logo():
    if current_user.is_authenticated:
        pass
    else:
        admin = Admin()
        admin.username = 'admin'
        admin.password = '123456'
        db.session.add(admin)
        db.session.commit()
        login_user(admin, remember=True)
    return render_template('base.html')


@login.route("/autologin")
def login_flash():
    flash("You have been automatically logged in~", 'primary')
    flash("Username: admin  Password: 123456", 'primary')

    return redirect(url_for('login.logo'))


@login.route("/hidden")
def hidden():
    flash("Congratulations on finding the hidden function! But nothing happens~", 'info')

    return redirect(url_for('login.logo'))
