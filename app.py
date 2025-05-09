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

with app.app_context():
    db.drop_all()
    db.create_all()
    create_fake_data(num_articles=500, num_authors=20, num_tags=15)

app.register_blueprint(article_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(author_blueprint)
app.register_blueprint(tag_blueprint)




if __name__ == '__main__':
    app.run(debug=True)
