from flask import *
from flask_login import current_user
from ..extension import db
from MLI.models import Preprocessing, Admin
from MLI.forms.preprocessing import PreForm

preprocessing = Blueprint("preprocessing", __name__)


@preprocessing.route('/pre', methods=["POST"])
def preprocess():
    form = PreForm()
    id_list = list()  # store chosen preprocess
    if form.Standardization.data:
        pre = Preprocessing.query.filter_by(preprocessing_name='Standardization').first()
        id_list.append(pre.id)
    admin = Admin.query.filter_by(id=current_user.id).first()
    admin.preprocessing_option = None if len(id_list) < 1 else id_list[0]  # commit the first one
    db.session.commit()
    flash("Excellent choice! Move on~", 'info')
    return redirect(url_for('algorithm.show_lr', id=admin.algorithm_option))
