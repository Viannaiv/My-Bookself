from application import db
from application.models import Base
from sqlalchemy.sql import text

WorkCategory = db.Table('WorkCategory',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(Base):
    works_category = db.relationship("Work", secondary=WorkCategory, back_populates="categories")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def works_in_category(category_id):
        stmt = text('SELECT Work.id, Work.name FROM Work'
                    ' LEFT JOIN "WorkCategory" ON "WorkCategory".work_id = Work.id'
                    ' LEFT JOIN Category ON "WorkCategory".category_id = Category.id'
                    ' WHERE Category.id = :c_id'
                    ' ORDER BY Work.name').params(c_id=category_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        if not response:
            response.append({"id":-10, "name":"no works found"})

        return response