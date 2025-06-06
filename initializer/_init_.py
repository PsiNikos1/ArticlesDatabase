from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
    db.init_app(app)
    ma.init_app(app)
