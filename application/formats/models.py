from application import db
from application.models import Base

class Format(Base):
    editions = db.relationship("Edition", backref='format', lazy=True)


    def __init__(self, name):
        self.name = name

        #Add format changing possibility
        #Add to format to edition info