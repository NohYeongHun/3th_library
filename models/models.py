from app import db
import datetime


class rabbitUser(db.Model):
    __tablename__ ='user'

    id = db.Column(db.String(20), primary_key=True, nullable=False )
    pw = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20))

class rabbitBook(db.Model):
    __tablename__ ='book'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name = db.Column(db.String(256), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publication_date = db.Column(db.DateTime)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    link = db.Column(db.String(200), nullable=False)
