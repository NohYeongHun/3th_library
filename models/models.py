from app import db
from datetime import datetime


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

class rabbitInventory(db.Model):
    __tablename__ ='inventory'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('rabbitBook.id'), nullable=False)
    exist_check = db.Column(db.Boolean, nullable=False, default=True)



class rabbitRent(db.Model):

    __tablename__ ='rent'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('rabbitInventory.id'), nullable=False)
    book_info_id = db.Column(db.Integer, db.ForeignKey('rabbitBook.id'), nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('rabbitUser.id'), nullable=False)
    # 빌린 날짜
    rent_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # 마감 예정일
    due_date = db.Column(db.DateTime, nullable=False)
    # 실제 반납일
    return_date = db.Column(db.DateTime, nullable=True)
    # 반납 여부
    book_return = db.Column(db.Boolean, nullable=False, default= False)

class rabbitComment(db.Model):

    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('rabbitUser.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('rabbitBook.id'),nullable=False)
    comment = db.Column(db.String(255))
    rating = db.Column(db.Integer)

    