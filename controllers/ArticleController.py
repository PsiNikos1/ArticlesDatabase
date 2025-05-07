from flask import Blueprint, app, jsonify

from initializer.TablesRelations import article_tags
from model.Article import Article


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

    def delete_article(self):
        """
        User can delete their own articles
        :return:
        """

    def create_article(self):
        """
        Creates a new article
        :return:
        """

