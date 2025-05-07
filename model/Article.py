from initializer.TablesRelations import article_authors, article_tags
from initializer._init_ import db
from model.Comment import Comment


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    abstract = db.Column(db.Text)
    publication_date = db.Column(db.Date)

    authors = db.relationship('Author', secondary=article_authors, backref='articles')
    tags = db.relationship('Tag', secondary=article_tags, backref='articles')
    comments = db.relationship('Comment', backref='article', cascade="all, delete-orphan")


    def to_dict(self):
        return {
            "id": self.id,
            "identifier": self.identifier,
            "title": self.title,
            "abstract": self.abstract,
            "publication_date": self.publication_date,
            "authors": [author.to_dict() for author in self.authors]
        }



