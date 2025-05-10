from flask import jsonify, request

from initializer._init_ import db
from model.Author import Author


class AuthorController:

    def getAllAuthors(self):
        authors = Author.query.all()
        return jsonify([author.to_dict() for author in authors])

    def create_author(self):
        data = request.json

        new_author = Author(name=data["name"])
        db.session.add(new_author)
        db.session.commit()

        return jsonify({"message": "Author created", "id": new_author.id}), 201

    def update_author(self):
        data = request.json
        author = Author.query.get_or_404(data["id"])

        new_name = data.get("name")
        if not new_name:
            return jsonify({"error": "Missing 'name' field"}), 400

        author.name = new_name
        db.session.commit()

        return jsonify({"message": "Author updated"}), 204

    def delete_author(self):
        data = request.json
        author_id = data.get("author_id")
        author = Author.query.get_or_404(author_id)
        db.session.delete(author)
        db.session.commit()
        return jsonify({"message": f"Author with id {author.id} deleted"})


