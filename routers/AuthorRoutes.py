from flask import Blueprint

from controllers.AuthorController import AuthorController

author_blueprint = Blueprint('authors', __name__, url_prefix='/author')

controller = AuthorController()

author_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.getAllAuthors)
