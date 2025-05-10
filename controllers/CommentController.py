from flask import jsonify, request
from jinja2.runtime import new_context

from initializer._init_ import db
from model.Comment import Comment


class CommentController:

    def create_comment(self):
        data = request.json

        if not data.get("article_id") or not data.get("user") or not data.get("content"):
            return jsonify({"error": "Missing required fields"}), 400

        comment = Comment(
            content=data["content"],
            user=data["user"],
            article_id=data["article_id"]
        )

        db.session.add(comment)
        db.session.commit()

        return jsonify({"message": "Comment created", "id": comment.id}), 201


    def update_comment(self):
        """
        User can Update comments on any article. Should only change the content.
        :return:
        """
        data = request.json
        comment = Comment.query.get_or_404(data["id"])
        if data["user"] != comment.user:
            return jsonify({"error": "Action is forbidden"}), 403
        new_content = data["content"]
        if not new_content:
            return jsonify({"error": "Missing 'content' field"}), 400
        comment.content = new_content
        db.session.commit()
        return jsonify({"message": "Comment updated"}), 200


    def delete_comment(self):
        """
        User can Delete comments on any article
        :return:
        """
        data = request.json
        comment = Comment.query.get_or_404(data["id"])
        if data["user"] != comment.user:
            return jsonify({"error": "Action is forbidden"}), 403
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": f"Author with id {comment.id} deleted"})

    def get_comments(self):
        """
        User can Get comments on any article
        :return:
        """
        data = request.json
        article_id = data.get("article_id", None)
        if not article_id:
            return  jsonify("article_id was not given"), 500
        comments = Comment.query.filter_by(article_id=article_id).all()
        return jsonify([comment.to_dict() for comment in comments])

    def get_all_comments(self):
        """
        Get all comments on a specific article
        :return:
        """
        comments = Comment.query.all()
        return jsonify([comment.to_dict() for comment in comments])