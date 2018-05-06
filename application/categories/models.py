from application import db
from application.models import Base

class Category(Base):

    def __init__(self, name):
        self.name = name

WorkCategory = db.Table('WorkCategory',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

#Here the methods for searching related works