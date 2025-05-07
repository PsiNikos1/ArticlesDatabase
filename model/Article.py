from initializer.TablesRelations import article_authors, article_tags
from initializer._init_ import db


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    abstract = db.Column(db.Text)
    publication_date = db.Column(db.Date)

    # #Set relationships
    authors = db.relationship('Author', secondary=article_authors, backref='articles')
    tags = db.relationship('Tag', secondary=article_tags, backref='articles')
    comments = db.relationship('Comment', backref='article', cascade="all, delete-orphan")


    def to_dict(self):
        return {
            "id": self.id,
            "identifier": self.name,
            "title": self.name,
            "abstract": self.name,
            "publication_date": self.name
        }



