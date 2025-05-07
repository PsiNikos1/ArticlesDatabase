from flask import Blueprint

from controllers.CommentController import CommentController

comment_blueprint = Blueprint('comments', __name__)

controller = CommentController()

# comment_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.get_all_articles)
