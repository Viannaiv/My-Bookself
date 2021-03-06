﻿from application import db
from application.models import Base

from sqlalchemy.sql import text

class Role(Base):

    def __init__(self, id, name):
        self.id = id
        self.name = name

class User(Base):

    __tablename__ = "account"
    
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    editions = db.relationship("Edition", backref='account', lazy=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)


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

    def roles(self):
        role = Role.query.get(self.role_id)
        return [role.name]

    @staticmethod
    def users_count():
        stmt = text("SELECT COUNT(DISTINCT Account.id), COUNT(DISTINCT Edition.id) FROM Account"
                    " LEFT JOIN Edition ON Edition.account_id = Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"usercount":row[0], "editions":row[1]})

        if not response:
            response.append({"usercount":"0", "editions":"0"})

        return response