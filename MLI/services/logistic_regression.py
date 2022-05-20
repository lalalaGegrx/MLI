from flask_login import current_user
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import f1_score, confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MLI.services.preprocessing import tr_te_split


def plot_matrix(y_true, y_pred, labels_name, thresh=0.8, axis_labels=None):
    cm = confusion_matrix(y_true, y_pred, labels=labels_name, sample_weight=None)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig = plt.figure()
    fig.patch.set_facecolor('#F8F8D9')
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#F8F8D9')
    plt.imshow(cm, interpolation='nearest', cmap=plt.get_cmap('Blues'))
    plt.colorbar()

    num_local = np.array(range(len(labels_name)))
    if axis_labels is None:
        axis_labels = labels_name
    plt.xticks(num_local, axis_labels, rotation=45)
    plt.yticks(num_local, axis_labels)
    plt.ylabel('Label')
    plt.xlabel('Prediction')

    for i in range(np.shape(cm)[0]):
        for j in range(np.shape(cm)[1]):
            if int(cm[i][j] * 100 + 0.5) > 0:
                plt.text(j, i, format(int(cm[i][j] * 100 + 0.5), 'd') + '%', ha="center", va="center",
                         color="white" if cm[i][j] > thresh else "black")

    fig.savefig('static/{}.png'.format(current_user.id))


def logistic_regression(dataset_fun, prepro_fun_list):
    features, data_x, data_y = dataset_fun()
    for fun in prepro_fun_list:
        data_x, data_y = fun(data_x, data_y)
    x_train, x_test, y_train, y_test = tr_te_split(data_x, data_y)
    y_train = y_train.values.ravel()
    y_test = y_test.values.ravel()
    lg_regress_model = LR()
    lg_regress_model.fit(x_train, y_train)
    y_predict = lg_regress_model.predict(x_test)
    accu = ((y_predict == y_test).sum() / len(y_test)).round(4)
    cross = cross_val_score(lg_regress_model, x_test, y_test, scoring='accuracy').mean().round(4)

    label = [0, 1, 2]
    f1 = f1_score(y_predict, y_test, labels=label, average="micro").round(4)
    plot_matrix(y_test, y_predict, label)

    fig = plt.figure()
    fig.patch.set_facecolor('#F8F8D9')
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#F8F8D9')

    x_display = np.around(np.array(x_test)[:10, :], decimals=4)
    y_test_display = np.around(np.array(y_test)[:10], decimals=4)
    y_pre_display = np.around(np.array(y_predict)[:10], decimals=4)

    thre = int(x_test.shape[0] * 0.5)
    x_personal = np.around(np.array(x_test)[thre: thre+10, :], decimals=4)
    y_personal = np.around(np.array(y_predict)[thre: thre+10], decimals=4)

    return features, x_display, y_test_display, y_pre_display, accu, cross, f1, x_personal, y_personal
