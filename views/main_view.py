from operator import ge
from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from function.validatio_check import *

bp = Blueprint('main', __name__, url_prefix='/')
    
    
@bp.route('/')
def home():
    return render_template('login.html')

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
            session['name'] = user_data.user_name

            flash("로그인 성공")
            return redirect(url_for('main.home'))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

