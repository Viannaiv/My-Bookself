from application import db
from application.models import Base

class Edition(Base):
    printed = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(50),nullable=False)
    read = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.String(600), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    format_id = db.Column(db.Integer, db.ForeignKey('format.id'), nullable=False)

    def __init__(self, name, printed, publisher, language, read):
        self.name = name
        self.printed = printed
        self.publisher = publisher
        self.language = language
        self.read = read
        self.notes = "-"

# Change notes to be nullable later?