from flask import *
from flask_login import current_user
from ..extension import db
from MLI.models import Algorithm, Dataset, Admin
from MLI.forms.preprocessing import PreForm
from MLI.services import select_name, select_algorithm, select_dataset, select_preprocessing


algorithm = Blueprint("algorithm", __name__)
algorithm_type, algorithm_op_str, dataset_op_str, features, x, y_test, y_pre, x_personal, y_personal = [None] * 9
mse, r2, cross, accu, f1 = [None] * 5


@algorithm.route('/algorithm/<int:id>')
def show_lr(id):
    algorithm = Algorithm.query.filter_by(id=id).first()
    admin = Admin.query.filter_by(id=current_user.id).first()
    if admin:
        admin.algorithm_option = algorithm.id
        db.session.commit()
    else:
        flash("There's something wrong!")

    form = PreForm()

    return render_template('algorithm.html', form=form, name=algorithm.algorithm_name)


@algorithm.route('/algorithm/result/')
def cal_result():
    admin = Admin.query.filter_by(id=current_user.id).first()
    if admin:
        global algorithm_type, algorithm_op_str, dataset_op_str, features, x, y_test, y_pre
        global mse, r2, accu, cross, f1, x_personal, y_personal
        dataset_op = admin.dataset_option
        algorithm_op = admin.algorithm_option
        preprocess_op = list()
        if admin.preprocessing_option:
            preprocess_op.append(admin.preprocessing_option)

        algo = Algorithm.query.filter_by(id=algorithm_op).first()
        data = Dataset.query.filter_by(id=dataset_op).first()
        if algo.type == 2 or algo.type == data.type:
            algorithm_type = algo.type
            algorithm_op_str, dataset_op_str, preprocess_op_str = select_name(dataset_op, algorithm_op, preprocess_op)
            algorithm_fun = select_algorithm(algorithm_op_str)
            dataset_fun = select_dataset(dataset_op_str)
            prepro_fun_list = select_preprocessing(preprocess_op_str)

            if algorithm_type:
                features, x, y_test, y_pre, accu, cross, f1, x_personal, y_personal = algorithm_fun(dataset_fun, prepro_fun_list)
            else:
                features, x, y_test, y_pre, mse, r2, cross, x_personal, y_personal = algorithm_fun(dataset_fun, prepro_fun_list)

            return redirect(url_for('algorithm.show_result', pid=0))

        flash("{} is not suitable for {}. Reselect algorithm or dataset.".format(data.dataset_name, algo.algorithm_name), 'danger')

        return redirect(url_for("algorithm.show_lr", id=algorithm_op))


@algorithm.route('/algorithm/result/<int:pid>')
def show_result(pid):
    global algorithm_type, algorithm_op_str, dataset_op_str, features, x, y_test, y_pre
    global mse, r2, accu, cross, f1, x_personal, y_personal
    if algorithm_type:
        return render_template('result_classify.html', features=features, x=x, y_test=y_test, y_pre=y_pre, accu=accu, cross=cross, f1=f1,
                               algorithm_name=algorithm_op_str, dataset_name=dataset_op_str,
                               x_personal=x_personal[pid], y_personal=y_personal[pid], pid=(pid+1) % 10, userid=current_user.id)
    else:
        return render_template('result.html', features=features, x=x, y_test=y_test, y_pre=y_pre, mse=mse, r2=r2, cross=cross,
                               algorithm_name=algorithm_op_str, dataset_name=dataset_op_str,
                               x_personal=x_personal[pid], y_personal=y_personal[pid], pid=(pid+1) % 10, userid=current_user.id)
