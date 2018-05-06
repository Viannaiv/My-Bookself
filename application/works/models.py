from application import db
from application.models import Base

class Work(Base):
    published = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)

    def __init__(self, name, published, description):
        self.name = name
        self.published = published
        self.description = description

# add BC and AD?
#here methods for searching related categories and authors