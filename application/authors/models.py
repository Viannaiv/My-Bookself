from application import db
from application.models import Base

class Author(Base):
    editions = db.relationship("Edition", backref='format', lazy=True)


    def __init__(self, name):
        self.name = name