from flask import Blueprint

from controllers.ArticleController import ArticleController

article_blueprint = Blueprint('articles', __name__, url_prefix='/articles')

controller = ArticleController()

article_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.get_all_articles)
article_blueprint.add_url_rule('/create', methods=['POST'], view_func=controller.createArticle)
article_blueprint.add_url_rule('/update', methods=['PUT'], view_func=controller.update_article)
article_blueprint.add_url_rule('/delete/<int:article_id>', methods=['DELETE'], view_func=controller.delete_article)
article_blueprint.add_url_rule('/filter', methods=['GET'], view_func=controller.filter_article)
