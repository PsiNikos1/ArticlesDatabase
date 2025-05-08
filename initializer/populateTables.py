from datetime import datetime

from initializer._init_ import db
from model.Article import Article
from model.Author import Author
from model.Comment import Comment
from model.Tag import Tag


def populate_authors():
    authors = ["Lebron James", "Micheal Jordan", "Steph Curry", "Kareem Abdul Jabbar", "Dennis Rodman"]

    for name in authors:
        if not Author.query.filter_by(name=name).first():
            db.session.add(Author(name=name))

    db.session.commit()

def populate_articles_and_tags():
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
        db.session.add(article)


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

    db.session.commit()

def populate_comments():
    from model.Article import Article  # imported here to avoid circular import

    first_article = Article.query.filter_by(identifier="LBJ1").first()
    second_article = Article.query.filter_by(identifier="MJvsLBJ").first()

    if first_article:
        comment1 = Comment(content="Lebron is the best!", user="Steph Curry fan", article_id=first_article.id)
        comment2 = Comment(content="Kareem is the best! Go Kareem!", user="Kareem fan", article_id=first_article.id)
        db.session.add_all([comment1, comment2])

    if second_article:
        comment3 = Comment(content="Jordan is the best.", user="Jordan fan", article_id=second_article.id)
        db.session.add(comment3)

    db.session.commit()

def run_all_populations():
    populate_authors()
    populate_articles_and_tags()
    populate_comments()
