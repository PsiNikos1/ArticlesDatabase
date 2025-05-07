from datetime import datetime

from flask import jsonify, request

from initializer._init_ import db
from model.Article import Article
from model.Author import Author
from model.Tag import Tag


class ArticleController:

    def get_all_articles(self):
        """
        Get all articles by any user
        :return:
        """
        articles = Article.query.all()
        return jsonify([article.to_dict() for article in articles])

    def filter_articles(self) -> list:
        """
        User can filter that list by year, month, author(s), tag(s) and keywords
        :return: A list of Articles
        """



    def update_article(self):
        """
        User can update their own articles
        :return:
        """


        data = request.json
        article_id = data["id"]
        article = Article.query.get_or_404(article_id)

        article.title = data.get("title", article.title)
        article.abstract = data.get("abstract", article.abstract)

        pub_date = data.get("publication_date")
        if pub_date:
            article.publication_date = datetime.strptime(pub_date, "%Y-%m-%d")

        # Update authors
        if "authors" in data:
            article.authors = []
            for name in data["authors"]:
                author = Author.query.filter_by(name=name).first()
                if not author:
                    author = Author(name=name)
                    db.session.add(author)
                article.authors.append(author)

        # Update tags
        if "tags" in data:
            article.tags = []
            for name in data["tags"]:
                tag = Tag.query.filter_by(name=name).first()
                if not tag:
                    tag = Tag(name=name)
                    db.session.add(tag)
                article.tags.append(tag)

        db.session.commit()
        return jsonify({"message": "Article updated", "id": article.id})



    def delete_article(self, article_id):
        """
        User can delete their own articles by it unique id
        :return:
        """
        article = Article.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()
        return jsonify({"message": f"Author with id {article.id} deleted"})


    def createArticle(self):
        data = request.json

        # Parse and create Article
        article = Article(
            identifier=data["identifier"],
            title=data["title"],
            abstract=data.get("abstract"),
            publication_date=datetime.strptime(data["publication_date"], "%Y-%m-%d")
        )
        db.session.add(article)

        article.authors = []
        for name in data.get("authors", []):
            author = Author.query.filter_by(name=name).first()
            if not author:
                author = Author(name=name)
                db.session.add(author)
            article.authors.append(author)

        article.tags = []
        for name in data.get("tags", []):
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            article.tags.append(tag)

        db.session.commit()

        return jsonify({"message": "Article created", "id": article.id}), 201
