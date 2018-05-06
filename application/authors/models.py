from application import db
from application.models import Base

AuthorWork = db.Table('AuthorWork',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Author(Base):
    works_author = db.relationship("Work", secondary=AuthorWork, back_populates="authors")

    def __init__(self, name):
        self.name = name



#Here the methods for searching related works