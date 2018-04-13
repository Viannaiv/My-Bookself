from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    editions = db.relationship("Edition", backref='account', lazy=True)


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def users_with_no_books():
        stmt = text("SELECT COUNT(Account.id) FROM Account"
                     " LEFT JOIN Edition ON Edition.account_id = Account.id"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Edition.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response