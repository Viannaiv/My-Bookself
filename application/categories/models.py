from application import db
from application.models import Base

WorkCategory = db.Table('WorkCategory',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(Base):
    works_category = db.relationship("Work", secondary=WorkCategory, back_populates="categories")

    def __init__(self, name):
        self.name = name

#Here the methods for searching related works