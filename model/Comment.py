from initializer._init_ import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "article_id": self.article_id        }
