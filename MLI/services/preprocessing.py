from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def standardscaler(x, y):
    scaler = StandardScaler()
    scaler.fit(x)
    x_std = scaler.transform(x)
    # print(x_std.mean())
    # print(x_std.std())
    return x_std, y


def tr_te_split(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    for val in [y_train, y_test]:
        val.index = range(val.shape[0])

    return x_train, x_test, y_train, y_test
