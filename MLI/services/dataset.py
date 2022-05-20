from sklearn.datasets import fetch_california_housing as fch
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_wine
from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd


def house_data():  # return data_head data_num features
    house_features = fch().feature_names
    house_price_x = pd.DataFrame(fch().data)
    house_price_y = pd.DataFrame(fch().target)
    size = house_price_x.shape[0]

    house_price_x = np.around(house_price_x.head().to_numpy(), decimals=4)
    house_price_y = np.around(house_price_y.head().to_numpy(), decimals=4)

    return size, house_features, house_price_x, house_price_y


def house_data_full():  # return data_head data_num features
    house_features = fch().feature_names
    house_price_x = pd.DataFrame(fch().data)
    house_price_y = pd.DataFrame(fch().target)

    return house_features, house_price_x, house_price_y


def diabetes_data():
    diabetes_features = load_diabetes().feature_names
    diabetes_x = pd.DataFrame(load_diabetes().data)
    diabetes_y = pd.DataFrame(load_diabetes().target)
    size = diabetes_x.shape[0]

    diabetes_x = np.around(diabetes_x.head().to_numpy(), decimals=4)
    diabetes_y = np.around(diabetes_y.head().to_numpy(), decimals=4)

    return size, diabetes_features, diabetes_x, diabetes_y


def diabetes_data_full():  # return data_head data_num features
    diabetes_features = load_diabetes().feature_names
    diabetes_x = pd.DataFrame(load_diabetes().data)
    diabetes_y = pd.DataFrame(load_diabetes().target)

    return diabetes_features, diabetes_x, diabetes_y


def wine_data():
    wine_features = load_wine().feature_names
    wine_x = pd.DataFrame(load_wine().data)
    wine_y = pd.DataFrame(load_wine().target)
    size = wine_x.shape[0]

    wine_x = np.around(wine_x.head().to_numpy(), decimals=4)
    wine_y = np.around(wine_y.head().to_numpy(), decimals=4)

    return size, wine_features, wine_x, wine_y


def wine_data_full():  # return data_head data_num features
    wine_features = load_wine().feature_names
    wine_x = pd.DataFrame(load_wine().data)
    wine_y = pd.DataFrame(load_wine().target)

    return wine_features, wine_x, wine_y
