from application import db
from application.models import Base
from application.categories.models import WorkCategory
from application.authors.models import AuthorWork
from sqlalchemy.sql import text

class Work(Base):
    published = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    categories = db.relationship("Category", secondary=WorkCategory, back_populates="works_category")
    authors = db.relationship("Author", secondary=AuthorWork, back_populates="works_author")

    def __init__(self, name, published, description):
        self.name = name
        self.published = published
        self.description = description

    @staticmethod
    def authors_of_work(work_id):
        stmt = text('SELECT Author.id, Author.name FROM Author'
                    ' LEFT JOIN "AuthorWork" ON "AuthorWork".author_id = Author.id'
                    ' LEFT JOIN Work ON "AuthorWork".work_id = Work.id'
                    ' WHERE Work.id = :w_id'
                    ' ORDER BY Author.name').params(w_id=work_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        if not response:
            response.append({"id":-10, "name":"no authors found"})

        return response

    @staticmethod
    def categories_of_work(work_id):
        stmt = text('SELECT Category.id, Category.name FROM Category'
                    ' LEFT JOIN "WorkCategory" ON "WorkCategory".category_id = Category.id'
                    ' LEFT JOIN Work ON "WorkCategory".work_id = Work.id'
                    ' WHERE Work.id = :w_id').params(w_id=work_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        if not response:
            response.append({"id":-10, "name":"no categories found"})

        return response