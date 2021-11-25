from operator import ge
from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from function.calc import avg_calc
import datetime

bp = Blueprint('rent', __name__, url_prefix='/rent')

@bp.route('/')
def home():

    # 현재 접속한 사용자의 대여 정보를 가져온다. 
    rent_list = rabbitRent.query\
        .join(rabbitBook, rabbitRent.book_info_id == rabbitBook.id)\
        .add_columns(
            rabbitRent.rent_date, rabbitRent.due_date, rabbitRent.book_return, rabbitRent.book_id,
            rabbitBook.book_name, rabbitBook.id
        ).filter(rabbitRent.user_id == session['user_id'])\
        .filter(rabbitRent.book_return ==False)
    
    rating_list = {} # 레이팅 점수
    book_list = rabbitBook.query.order_by(rabbitBook.id.asc())
    for book in book_list:
        
        try:
            # rating 계산 
            ratings = rabbitComment.query.filter(rabbitComment.book_id == book.id).with_entities(rabbitComment.rating).all()
            avg = avg_calc(ratings)
            rating_list[book.id]= avg
            
        except:
            rating_list[book.id] = 0
    
    page = request.args.get('page', type=int, default=1) # 페이지
    page_list = rent_list.paginate(page, per_page = 8)
    
    return render_template('rent.html', page_list=page_list, rating_list=rating_list)

@bp.route('/book_return/<int:book_id>',methods=["POST"] )
def book_return(book_id):

    # 책을 반납.
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    try:
        inventory = rabbitInventory.query.filter((rabbitInventory.id == book_id) & (rabbitInventory.exist_check==False)).first()
        inventory.query.filter(rabbitInventory.id == book_id).update({"exist_check":(True)})
        rabbitRent.query.filter(rabbitRent.book_id == book_id).update({"book_return":(True)})
        rabbitRent.query.filter(rabbitRent.book_id == book_id).update({"return_date":(nowDate)})
        db.session.commit()
        flash("책이 정상적으로 반납되었습니다.")
    except:
        flash("반납 과정에서 오류가 있었습니다.")

    return redirect(url_for("rent.home"))


@bp.route('/rent_record/<string:user_id>')
def book_record(user_id):
    '''
    대여 기록에 대한 코드.
    '''
    rent_list = rabbitRent.query\
        .join(rabbitBook, rabbitRent.book_info_id == rabbitBook.id)\
        .add_columns(
            rabbitRent.rent_date, rabbitRent.due_date, rabbitRent.book_return, rabbitRent.book_id, rabbitRent.return_date,
            rabbitBook.book_name, rabbitBook.id
        ).filter(rabbitRent.user_id == user_id)

    book_list = rabbitBook.query.order_by(rabbitBook.id.asc())
    rating_list = {} # 레이팅 점수
    for book in book_list:
        
        try:
            # rating 계산 
            ratings = rabbitComment.query.filter(rabbitComment.book_id == book.id).with_entities(rabbitComment.rating).all()
            avg = avg_calc(ratings)
            rating_list[book.id]= avg
            
        except:
            rating_list[book.id] = 0

    page = request.args.get('page', type=int, default=1) # 페이지
    page_list = rent_list.paginate(page, per_page = 8)

    return render_template('rent_record.html', page_list = page_list, rating_list = rating_list)