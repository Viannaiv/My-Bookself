from application import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    published = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)

    def __init__(self, name, published, description):
        self.name = name
        self.published = published
        self.description = description