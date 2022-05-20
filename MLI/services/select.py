from MLI.models import Algorithm, Dataset, Preprocessing
from MLI.services import linear_regression, logistic_regression
from MLI.services import house_data_full, diabetes_data_full, wine_data_full
from MLI.services import standardscaler


def select_name(dataset_op, algorithm_op, preprocess_op):
    algorithm = Algorithm.query.filter_by(id=algorithm_op).first()
    algorithm_name = algorithm.algorithm_name
    dataset = Dataset.query.filter_by(id=dataset_op).first()
    dataset_name = dataset.dataset_name
    preprocess_name = list()
    for id in preprocess_op:
        tmp = Preprocessing.query.filter_by(id=id).first()
        preprocess_name.append(tmp.preprocessing_name)

    return algorithm_name, dataset_name, preprocess_name


def select_algorithm(algorithm_name):
    if algorithm_name == "Linear Regression":
        return linear_regression
    if algorithm_name == "Logistic Regression":
        return logistic_regression

    return None


def select_dataset(dataset_name):
    if dataset_name == "California Housing Price Dataset":
        return house_data_full
    if dataset_name == "Diabetes Dataset":
        return diabetes_data_full
    if dataset_name == "Wine Dataset":
        return wine_data_full

    return None


def select_preprocessing(preprocess_name):
    preprocess_fun = list()
    if "Standardization" in preprocess_name:
        preprocess_fun.append(standardscaler)

    return preprocess_fun

