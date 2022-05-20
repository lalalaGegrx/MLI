from ..extension import db


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataset_name = db.Column(db.String(100), unique=True)
    type = db.Column(db.Integer)

    def __repr__(self):
        return "<Dataset: {}-{}>".format(Dataset.id, Dataset.dataset_name)


class Preprocessing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preprocessing_name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<Preprocessing: {}-{}>".format(Preprocessing.id, Preprocessing.preprocessing_name)


class Algorithm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithm_name = db.Column(db.String(100), unique=True)
    type = db.Column(db.Integer)

    def __repr__(self):
        return "<Algorithm: {}-{}>".format(Algorithm.id, Algorithm.algorithm_name)
