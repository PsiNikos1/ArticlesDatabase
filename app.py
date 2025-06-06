from flask import Flask

from initializer import populateTables
from initializer._init_ import init_db, db
from initializer.populateTables import create_fake_data
from model.Article import Article
from model.Author import Author
from model.Comment import Comment
from model.Tag import Tag
from routers.ArticleRoutes import article_blueprint
from routers.AuthorRoutes import author_blueprint
from routers.CommentRoutes import comment_blueprint
from routers.TagRoutes import tag_blueprint

app = Flask(__name__)
init_db(app)

app.register_blueprint(article_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(author_blueprint)
app.register_blueprint(tag_blueprint)




if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
