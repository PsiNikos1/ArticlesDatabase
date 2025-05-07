from flask import Blueprint

from controllers.AuthorController import AuthorController

author_blueprint = Blueprint('authors', __name__)

controller = AuthorController()

author_blueprint.add_url_rule('/getAllAuthors', methods=['GET'], view_func=controller.getAllAuthors)
