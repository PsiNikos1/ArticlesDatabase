from flask import Flask

from initializer._init_ import init_db, db
from initializer.populateTables import create_fake_data

app = Flask(__name__)
init_db(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    create_fake_data(num_articles=500, num_authors=20, num_tags=15)
