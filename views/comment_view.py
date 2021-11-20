from operator import ge
from flask import Blueprint, render_template, request,session,url_for, redirect, flash
from models.models import *


bp = Blueprint('comment', __name__, url_prefix='/comment')

'''
    설명 : id 값에 맞는 책 정보를 가져온다.
'''
@bp.route('/<int:id>')
def home(id):
    
    # 책의 id값의 정보들
    book_info = rabbitBook.query.filter(rabbitBook.id == id).first()
  
    # 평가가 없을수도 있음.
    comment_list = []
    try:
        # 리스트로 반환됨.
        comments = rabbitComment.query.filter(rabbitComment.book_id == id).all()
        user_name = rabbitUser.query.filter(rabbitUser.id == comments.user_id).all()
    except:
        flash("평가가 없습니다.")
        comments = None
        user_name = None

    
    print(user_name)
    
    

    return render_template(
        'comment.html', 
        book_info = book_info,
        user_name = user_name,
        comments = comments
    )

@bp.route('/submit/<int:id>',methods=["POST"])
def submit(id):

    try:
        comment = request.form['comment']
        rating = request.form['rate']
    except:
        flash("제출하시려면 평점과 댓글을 모두 작성해 주세요.")

    user_id = session['user_id']

    book_id = id

    postComment = rabbitComment(
        user_id= user_id, 
        book_id= book_id, 
        comment= comment, 
        rating = rating
    )
    db.session.add(postComment)
    db.session.commit()

    #DB write
    # post = rabbitComment(rating, comment)
    # db.session.add(post)
    # db.session.commit()

    return redirect(url_for('comment.home',id=id))