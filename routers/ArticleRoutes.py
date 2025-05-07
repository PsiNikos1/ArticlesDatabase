from flask import Blueprint

from controllers.ArticleController import ArticleController

article_blueprint = Blueprint('articles', __name__, url_prefix='/article')

controller = ArticleController()

article_blueprint.add_url_rule('/getAll', methods=['GET'], view_func=controller.get_all_articles)
