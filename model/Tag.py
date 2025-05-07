from initializer._init_ import db



class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content
        }

