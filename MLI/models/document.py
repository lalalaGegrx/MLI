from ..extension import db

from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)

    comments = db.relationship('Comment', back_populate='article', cascade='all')

    def __repr__(self):
        return "<Article: {}-{}>".format(self.author, self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    article_id = db.Column(db.Integer, db.ForeignKey('Article.id'))
    article = db.relationship('Article', back_populate='comments')

    def __repr__(self):
        return "<Comment {}-{}>".format(self.article_id, self.id)
