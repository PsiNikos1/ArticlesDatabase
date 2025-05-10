from flask import Blueprint

from controllers.TagController import TagController

tag_blueprint = Blueprint('tags', __name__, url_prefix='/tags')

controller = TagController()

tag_blueprint.add_url_rule('/getAll/page/<int:page_number>', methods=['GET'], view_func=controller.get_all_tags)
tag_blueprint.add_url_rule('/create', methods=['POST'], view_func=controller.create_tag)
tag_blueprint.add_url_rule('/delete', methods=['DELETE'], view_func=controller.delete_tag)
tag_blueprint.add_url_rule('/update', methods=['PUT'], view_func=controller.update_tag)



