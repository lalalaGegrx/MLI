from flask_login import current_user
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MLI.services.preprocessing import tr_te_split


def linear_regression(dataset_fun, prepro_fun_list):
    features, data_x, data_y = dataset_fun()
    for fun in prepro_fun_list:
        data_x, data_y = fun(data_x, data_y)
    x_train, x_test, y_train, y_test = tr_te_split(data_x, data_y)
    lr_regress_model = LR()
    lr_regress_model.fit(x_train, y_train)
    y_predict = lr_regress_model.predict(x_test)

    mse = mean_squared_error(y_predict, y_test).round(4)
    r2 = r2_score(y_predict, y_test).round(4)
    cross = - cross_val_score(lr_regress_model, x_test, y_test, scoring='neg_mean_squared_error').mean().round(4)

    fig = plt.figure()
    fig.patch.set_facecolor('#F8F8D9')
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#F8F8D9')
    plt.plot(range(len(y_test)), np.sort(np.array(y_test), axis=0), c='red', label='Label')
    plt.plot(range(len(y_predict)), np.sort(np.array(y_predict), axis=0), c='c', label='Prediction')
    plt.xlabel("Num of data")
    plt.ylabel("Price")
    plt.legend()
    fig.savefig('static/{}.png'.format(current_user.id))

    x_display = np.around(np.array(x_test)[20: 30, :], decimals=4)
    y_test_display = np.around(np.array(y_test)[20: 30, 0], decimals=4)
    y_pre_display = np.around(np.array(y_predict)[20: 30, 0], decimals=4)

    thre = int(x_test.shape[0] * 0.5)
    x_personal = np.around(np.array(x_test)[thre: thre+10, :], decimals=4)
    y_personal = np.around(np.array(y_predict)[thre: thre+10, 0], decimals=4)

    return features, x_display, y_test_display, y_pre_display, mse, r2, cross, x_personal, y_personal
