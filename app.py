from flask import Flask

from initializer import populateTables
from initializer._init_ import init_db, db
from routers.ArticleRoutes import article_blueprint
from routers.AuthorRoutes import author_blueprint
from routers.CommentRoutes import comment_blueprint
from routers.TagRoutes import tag_blueprint

app = Flask(__name__)
init_db(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    populateTables.populate_authors()
    populateTables.populate_articles_and_tags()
    populateTables.populate_comments()

app.register_blueprint(article_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(author_blueprint)
app.register_blueprint(tag_blueprint)




if __name__ == '__main__':
    app.run(debug=True)
