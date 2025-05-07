from datetime import datetime

from initializer._init_ import db
from model.Article import Article
from model.Author import Author
from model.Tag import Tag


def populate_authors():
    authors = ["Lebron James", "Micheal Jordan", "Steph Curry", "Kareem Abdul Jabbar", "Dennis Rodman"]

    for name in authors:
        if not Author.query.filter_by(name=name).first():
            db.session.add(Author(name=name))

    db.session.commit()

def populate_articles():
    articles = [
        {
            "identifier": "LBJ1",
            "title": "Most points in NBA history",
            "abstract": "This article explains is about LBJ becoming #1 in all time scoring list",
            "publication_date": "2023-02-07",
            "authors": ["Lebron James", "Kareem Abdul Jabbar"],
            "tags": ["NBA", "most_points"]
        },
        {
            "identifier": "MJvsLBJ",
            "title": "Who is the NBA GOAT",
            "abstract": "This article settles the GOAT debate once and for all.",
            "publication_date": "2024-06-20",
            "authors": ["Dennis Rodman", "Kareem Abdul Jabbar"],
            "tags": ["GOAT", "NBA"]
        }

    ]

    for data in articles:
        article = Article(
            identifier=data["identifier"],
            title=data["title"],
            abstract=data["abstract"],
            publication_date=datetime.strptime(data["publication_date"], "%Y-%m-%d")
        )

        article.authors = []
        for author_name in data["authors"]:
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)
            article.authors.append(author)

        article.tags = []
        for tag_name in data["tags"]:
            tag = Tag.query.filter_by(content=tag_name).first()
            if not tag:
                tag = Tag(content=tag_name)
                db.session.add(tag)
            article.tags.append(tag)

        db.session.add(article)
    db.session.commit()
