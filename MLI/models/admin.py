from flask_login import UserMixin
from ..extension import db


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    info = db.Column(db.Text)

    algorithm_option = db.Column(db.Integer)
    dataset_option = db.Column(db.Integer)
    preprocessing_option = db.Column(db.Integer)

    def __repr__(self):
        return "<Admin: {}-{}>".format(Admin.id, Admin.username)
