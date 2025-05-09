from faker import Faker
import random
from initializer._init_ import db
from model.Article import Article
from model.Author import Author
from model.Comment import Comment
from model.Tag import Tag

fake = Faker()

def create_fake_data(num_articles=50, num_authors=10, num_tags=10):
    # Step 1: Create Authors
    authors = []
    for _ in range(num_authors):
        author = Author(name=fake.name())
        db.session.add(author)
        authors.append(author)

    db.session.commit()

    tags = []
    for _ in range(num_tags):
        tag = Tag(content=fake.word())
        db.session.add(tag)
        tags.append(tag)

    db.session.commit()

    # Step 3: Create Articles
    articles = []
    for _ in range(num_articles):
        article = Article(
            title=fake.sentence(nb_words=6),
            abstract=fake.paragraph(nb_sentences=3),
            publication_date=fake.date_this_decade()
        )
        article.authors = random.sample(authors, k=random.randint(1, 3))
        article.tags = random.sample(tags, k=random.randint(1, 4))
        db.session.add(article)
        articles.append(article)

    db.session.commit()

    # Step 4: Add Comments
    for article in articles:
        for _ in range(random.randint(1, 5)):
            comment = Comment(
                content=fake.sentence(),
                user=fake.user_name(),
                article_id=article.id
            )
            db.session.add(comment)

    db.session.commit()
