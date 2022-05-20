from flask import *
from flask_login import current_user
from ..extension import db
from MLI.services.dataset import house_data, diabetes_data, wine_data
from MLI.models import Admin, Dataset, Algorithm

dataset = Blueprint('dataset', __name__)


@dataset.route('/dataset')
def show_dataset():
    datasum, tmp_dict = dict(), dict()
    for (i, f) in enumerate([house_data(), diabetes_data(), wine_data()]):
        size, tmp_features, tmp_x, tmp_y = f
        tmp_dict['features'] = tmp_features
        tmp_dict['X'] = tmp_x
        tmp_dict['y'] = tmp_y
        tmp_dict['size'] = size
        datasum[i+1] = tmp_dict.copy()

    return render_template('dataset.html', data=datasum)


@dataset.route('/dataset/<int:id>')
def choose_dataset(id):
    admin = Admin.query.filter_by(id=current_user.id).first()
    if admin:
        algorithm = Algorithm.query.filter_by(id=admin.algorithm_option).first()
        dataset = Dataset.query.filter_by(id=id).first()
        if algorithm.type == 2 or algorithm.type == dataset.type:
            admin.dataset_option = id
            db.session.commit()
            flash("You have chosen {}! Move on~".format(dataset.dataset_name), 'info')
        else:
            flash("{} is not suitable for {}. Reselect.".format(dataset.dataset_name, algorithm.algorithm_name), 'danger')
            return redirect(url_for('dataset.show_dataset'))
    else:
        flash("There's something wrong!", 'danger')
    return redirect(url_for('algorithm.show_lr', id=admin.algorithm_option))
