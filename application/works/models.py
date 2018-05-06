from application import db
from application.models import Base
from application.categories.models import WorkCategory
from application.authors.models import AuthorWork

class Work(Base):
    published = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    categories = db.relationship("Category", secondary=WorkCategory, back_populates="works_category")
    authors = db.relationship("Author", secondary=AuthorWork, back_populates="works_author")

    def __init__(self, name, published, description):
        self.name = name
        self.published = published
        self.description = description

#here methods for searching related categories and authors