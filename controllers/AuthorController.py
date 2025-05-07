from flask import jsonify

from model.Author import Author


class AuthorController:

    def getAllAuthors(self):
        authors = Author.query.all()
        return jsonify([author.to_dict() for author in authors])