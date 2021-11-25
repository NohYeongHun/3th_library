from operator import ge
from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from function.validation_check import *
from function.calc import avg_calc

bp = Blueprint('main', __name__, url_prefix='/')

   
    
@bp.route('/')
def home():

   
    book_list = rabbitBook.query.order_by(rabbitBook.id.asc())

    # dictionary 
    inventory_list={} # 재고 
    rating_list ={} # 레이팅 점수
    

     # rating 계산
    for book in book_list:
        try:
            # rating 계산
            ratings = rabbitComment.query.filter(rabbitComment.book_id == book.id).with_entities(rabbitComment.rating).all()
            avg = avg_calc(ratings)
            rating_list[book.id] = avg
            
        except:
            rating_list[book.id] = 0

    page = request.args.get('page', type=int, default=1) # 페이지
    page_list = book_list.paginate(page, per_page = 8)
    

    for book in book_list:
        # 재고 계산 exist_check == True인 책들의 재고를 계산한다.
        inventory = rabbitInventory.query.filter((rabbitInventory.book_id == book.id) & (rabbitInventory.exist_check==True)).all()
        inventory_list[book.id] = len(inventory)
        

    return render_template('main.html', page_list = page_list, rating_list = rating_list, inventory_list = inventory_list)

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
        
    elif request.method =='POST':
        # 회원가입 과정
        # 동일 아이디가 있는가?
        user = rabbitUser.query.filter_by(id=request.form['user_id']).first()
        if not user:

            password = request.form['password']
            password2 = request.form['password2'] # 비밀번호 확인
            user_id = request.form['user_id']
            user_name = request.form['user_name']

            # 아이디를 이메일형식으로 만들기.
            if register_email_check(user_id):
                pass
            else:
                flash("아이디를 이메일 형식으로 만들어야 합니다.")
                return redirect(url_for('main.register'))
            
            if register_name_check(user_name):
                pass
            else:
                flash("사용자 이름을 영문 또는 한글로만 표기해주세요.")
                return redirect(url_for('main.register'))

            # 패스워드 유효성 검사
            if register_password_check(password) and password2 == password:
                
                # 패스워드 암호화
                password = generate_password_hash(password)
                user = rabbitUser(id=user_id, pw=password,
                                user_name=user_name, telephone=request.form['telephone'])
                
                # session에 user를 추가(로그인 유지)
                db.session.add(user)
                db.session.commit()


                flash("회원가입이 완료되었습니다")
                return redirect(url_for("main.home"))

            else:
                flash("패스워드 유효성 검사에 실패하였습니다.")
                return redirect(url_for('main.register'))

        else:

            #동일 아이디가 있다면
            flash("이미 가입된 아이디입니다.")
            return redirect(url_for('main.register'))

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        id    = request.form['user_id']
        pw    = request.form['password']

        # id가 이메일 형태인지?
        if register_email_check(id):
            pass
        else:
            flash("아이디를 이메일 형식으로 입력해야 합니다.")
            return redirect(url_for('main.login'))
        

        # 패스워드가 형식에 맞는지?
        if register_password_check(pw):
            pass

        else:
            flash("패스워드를 형식에 맞게 입력해주세요")
            return redirect(url_for('main.login'))
        
        user_data = rabbitUser.query.filter_by(id=id).first()

        if not user_data:
            flash("없는 아이디입니다.")
            return redirect(url_for('main.login'))
            
        # password 복호화 이후 비교
        elif not check_password_hash(user_data.pw, pw):
            flash("비밀번호가 틀렸습니다.")
            return redirect(url_for('main.login'))
        else:
            session.clear()
            session['user_id'] = id
            session['user_name'] = user_data.user_name

            flash("로그인 성공")
            return redirect(url_for('main.home'))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))


@bp.route('/book_rent/<int:book_id>',methods=["POST"] )
def book_rent(book_id):

    # 만약 사용자가 이미 빌린책이라면? => 대여 불가
    check_rent = rabbitRent.query.filter(
            (rabbitRent.book_info_id == book_id) & (rabbitRent.user_id == session['user_id']) & (rabbitRent.book_return == False)
        ).first()

    if check_rent != None:
        flash("이미 해당 책을 대여하셨습니다.")
        return redirect(url_for('main.home'))
    else:
    
    # 대여하기 => 해당 id의 재고 감소
    # 재고가 없는 상황도 있음.
        try:
            # 대여하기를 누른 책의 id의 exist_check를 False로 변경해줌
            inventory = rabbitInventory.query.filter((rabbitInventory.book_id == book_id) & (rabbitInventory.exist_check==True)).first()
            inventory.query.filter(rabbitInventory.id == inventory.id).update({"exist_check":(False)})

            # 대여 정보 추가.
            rent = rabbitRent(
                book_id = inventory.id, 
                book_info_id = book_id, 
                user_id = session['user_id']
                )
            db.session.add(rent)
            db.session.commit()        
            
            flash("책이 정상적으로 대여되었습니다.")
        except:
            flash("해당 책은 재고가 없습니다.")
            
    
    
    
    return redirect(url_for('main.home'))