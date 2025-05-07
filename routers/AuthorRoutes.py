from flask import Blueprint

from controllers.AuthorController import AuthorController

author_blueprint = Blueprint('authors', __name__, url_prefix='/authors')

controller = AuthorController()

author_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.getAllAuthors)
author_blueprint.add_url_rule('/create', methods=['POST'], view_func=controller.create_author)
author_blueprint.add_url_rule('/update', methods=['PUT'], view_func=controller.update_author)
author_blueprint.add_url_rule('/delete/<int:author_id>', methods=['DELETE'], view_func=controller.delete_author)

