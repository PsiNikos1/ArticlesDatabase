import csv
from datetime import datetime
from io import BytesIO, StringIO

from flask import jsonify, request, send_file
from sqlalchemy import extract, or_

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
        return jsonify([article.to_dict() for article in articles]), 200

    def update_article(self):
        """
        User can update their own articles
        :return:
        """
        data = request.json
        article_id = data["id"]
        article = Article.query.get_or_404(article_id)

        if data["user"] not in [author.name for author in article.authors]:
            return jsonify({"error": "Unauthorized"}), 403


        article.title = data.get("title", article.title)
        article.abstract = data.get("abstract", article.abstract)
        article.identifier = data.get("abstract", article.identifier)

        # Update authors
        if "authors" in data:
            article.authors = []
            for author_data in data["authors"]:
                author = Author.query.filter_by(name=author_data["name"]).first()
                if not author:
                    author = Author(name=author_data["name"])
                    db.session.add(author)
                article.authors.append(author)

        # Update tags
        if "tags" in data:
            article.tags = []
            for tag_data in data["tags"]:
                tag = Tag.query.filter_by(content=tag_data["content"]).first()
                if not tag:
                    tag = Tag(content=tag_data["content"])
                    db.session.add(tag)
                article.tags.append(tag)

        db.session.commit()
        return jsonify({"message": "Article updated", "id": article.id})

    def delete_article(self):
        """
        User can delete their own articles by it unique id
        :return:
        """
        data = request.json
        article = Article.query.get_or_404(data["article_id"])
        if data["user"] not in [author.name for author in article.authors]:
            return jsonify({"error": "Unauthorized"}), 403

        db.session.delete(article)
        db.session.commit()
        return jsonify({"message": f"Article with id {article.id}  & title '{article.title}' has been deleted"})


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

    def filter_article(self):
        data = request.json
        query = Article.query

        for key, value in data.items():
            if key == "year":
                query = query.filter(extract("year", Article.publication_date) == value)

            elif key == "month":
                query = query.filter(extract("month", Article.publication_date) == value)

            elif key == "authors":
                author_ids = [a.get("id") for a in value if a.get("id")]
                if author_ids:
                    query = query.filter(Article.authors.any(Author.id.in_(author_ids)))

            elif key == "tags":
                tags_id = [a.get("id") for a in value if a.get("id")]
                if tags_id:
                    query = query.filter(Article.tags.any(Tag.id.in_(tags_id)))

            elif key == "title":
                query = query.filter(Article.title.ilike(f"%{value}%"))

            elif key == "abstract":
                query = query.filter(Article.abstract.ilike(f"%{value}%"))

            elif key == "identifier":
                query = query.filter(Article.identifier.ilike(f"%{value}%"))

            elif key == "keywords":
                keywords = value if isinstance(value, list) else [value]
                search_conditions = [
                    or_(
                        Article.title.ilike(f"%{kw}%"),
                        Article.abstract.ilike(f"%{kw}%")
                    )
                    for kw in keywords
                ]
                query = query.filter(or_(*search_conditions))

        results = query.all()
        return jsonify([a.to_dict() for a in results]), 200

    def download_filtered_articles_csv(self):
        data = request.json or {}
        query = Article.query

        for key, value in data.items():
            if key == "year":
                query = query.filter(extract("year", Article.publication_date) == value)

            elif key == "month":
                query = query.filter(extract("month", Article.publication_date) == value)

            elif key == "authors":
                author_ids = [a.get("id") for a in value if a.get("id")]
                if author_ids:
                    query = query.filter(Article.authors.any(Author.id.in_(author_ids)))

            elif key == "tags":
                tags_id = [a.get("id") for a in value if a.get("id")]
                if tags_id:
                    query = query.filter(Article.tags.any(Tag.id.in_(tags_id)))

            elif key == "title":
                query = query.filter(Article.title.ilike(f"%{value}%"))

            elif key == "abstract":
                query = query.filter(Article.abstract.ilike(f"%{value}%"))

            elif key == "identifier":
                query = query.filter(Article.identifier.ilike(f"%{value}%"))

            elif key == "keywords":
                keywords = value if isinstance(value, list) else [value]
                search_conditions = [
                    or_(
                        Article.title.ilike(f"%{kw}%"),
                        Article.abstract.ilike(f"%{kw}%")
                    )
                    for kw in keywords
                ]
                query = query.filter(or_(*search_conditions))

        articles = query.all()

        # Write CSV
        si = StringIO()
        writer = csv.writer(si)
        writer.writerow(["ID", "Title", "Abstract", "Publication Date", "Authors", "Tags"])

        for article in articles:
            writer.writerow([
                article.id,
                article.title,
                article.abstract,
                article.publication_date,
                "; ".join(a.name for a in article.authors),
                "; ".join(t.content for t in article.tags)
            ])

        output = BytesIO()
        output.write(si.getvalue().encode('utf-8'))
        output.seek(0)

        return send_file(
            output,
            mimetype="text/csv",
            as_attachment=True,
            download_name="filtered_articles.csv"
        )
