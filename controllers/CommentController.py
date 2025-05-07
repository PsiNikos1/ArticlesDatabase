from flask import jsonify, request
from jinja2.runtime import new_context

from initializer._init_ import db
from model.Comment import Comment


class CommentController:

    def create_comment(self):
        """
        User can Create comments on any article
        :return:
        """

    def update_comment(self):
        """
        User can Update comments on any article
        :return:
        """
        data = request.json
        comment = Comment.query.get_or_404(data["id"])
        new_content = data["content"]
        if not new_content:
            return jsonify({"error": "Missing 'content' field"}), 400
        comment.content = new_content
        db.session.commit()
        return jsonify({"message": "Comment updated"}), 204


    def delete_comment(self, comment_id):
        """
        User can Delete comments on any article
        :return:
        """
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": f"Author with id {comment.id} deleted"})

    def get_comments(self, article_id):
        """
        User can Get comments on any article
        :return:
        """
        comments = Comment.query.filter_by(article_id=article_id).all()
        return jsonify([comment.to_dict() for comment in comments])

    def get_all_comments(self):
        """
        Get all comments on a specific article
        :return:
        """
        comments = Comment.query.all()
        return jsonify([comment.to_dict() for comment in comments])