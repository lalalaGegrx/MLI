from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from MLI.models.admin import Admin
    user = db.session.query(Admin).get(user_id)
    return user
