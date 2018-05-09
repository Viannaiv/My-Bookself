from application import db
from application.models import Base
from sqlalchemy.sql import text

AuthorWork = db.Table('AuthorWork',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Author(Base):
    works_author = db.relationship("Work", secondary=AuthorWork, back_populates="authors")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def works_of_author(author_id):
        stmt = text("SELECT Work.id, Work.name, Work.published FROM Work"
                    " LEFT JOIN AuthorWork ON AuthorWork.work_id = Work.id"
                    " LEFT JOIN Author ON AuthorWork.author_id = Author.id"
                    " WHERE Author.id = 1"
                    " ORDER BY Work.published")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "published":row[2]})

        if not response:
            response.append({"username":"No works added yet"})

        return response