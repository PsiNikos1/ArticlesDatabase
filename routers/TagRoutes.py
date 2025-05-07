from flask import Blueprint

from controllers.CommentController import CommentController
from controllers.TagController import TagController

tag_blueprint = Blueprint('tags', __name__, url_prefix='/tags')

controller = TagController()

tag_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.get_all_tags)
