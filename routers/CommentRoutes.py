from flask import Blueprint

from controllers.CommentController import CommentController

comment_blueprint = Blueprint('comments', __name__, url_prefix='/comments')

controller = CommentController()

comment_blueprint.add_url_rule('/getComments', methods=['GET'], view_func=controller.get_comments)
comment_blueprint.add_url_rule('/delete/', methods=['DELETE'], view_func=controller.delete_comment)
comment_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.get_all_comments)
comment_blueprint.add_url_rule('/update', methods=['PUT'], view_func=controller.update_comment)
comment_blueprint.add_url_rule('/create', methods=['POST'], view_func=controller.create_comment)
