## 도서관 대출 서비스

### ToDo-List
| 항목                    |내용                                | 진행 여부                                                                                            |
|:-----------------------:|:----------------------------------:|:----------------------------------------------------------------------------------------------------:|
|로그인                   | 세션 로그인 유지, 로그인 규칙      | <ul><li> - [x] 세션 로그인 유지,</li><li> - [x] 로그인 규칙                                </li></ul>|
|회원가입                 | 개인정보 보호형식에 맞춘 회원가입  | <ul><li> - [x] 개인정보 보호형식에 맞춘 회원가입                                                </ul>|
|로그아웃                 | 세션을 통한 로그아웃               | <ul><li> - [x] 세션을 통한 로그아웃                                                        </li></ul>|
|DB 생성                  | DB 생성                            | <ul><li> - [x] DB 생성                                                                     </li></ul>|
|페이지네이션             | 각 페이지의 페이지네이션 구현      | <ul><li> - [x] 각 페이지 페이지네이션 구현                                                 </li></ul>|
|메인페이지               | 책의 평점표기,레이아웃             | <ul><li> - [x] 책의 평점 표기</li><li> - [x] 레이아웃 </li>                                     </ul>|
|반납하기                 | 페이지 레이아웃 구현, DB 로직 구현 | <ul><li> - [x] DB로직 구현</li><li> - [x] 페이지 레이아웃 구현</li>                             </ul>|
|대여기록                 | 페이지 레이아웃 구현, DB 로직 구현 | <ul><li> - [x] DB로직 구현</li><li> - [x] 페이지 레이아웃 구현</li>                             </ul>|


### 참고 사이트
|참고 내용                |참조 사이트                                                                                                        |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------------:|
|페이지네이션             |https://wikidocs.net/81054                                                                                         |
|라디오 버튼              |https://stackoverflow.com/questions/15839169/how-to-get-value-of-selected-radio-button                             |
|플라스크와html간 변수전달|https://velog.io/@dltpal07/flask%EC%99%80-html-%EA%B0%84%EC%9D%98-%EB%B3%80%EC%88%98-%EC%A0%84%EB%8B%AC            |
| 점수 아이콘 css         |https://www.codingnepalweb.com/star-rating-html-css-javascript/                                                    |
| button href 사용 예시   |https://www.codestudyblog.com/sf2002e/0224200636.html                                                              |
| 패스워드 정규식         |https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/                                 |
| MySQL 트리거            |https://stackoverflow.com/questions/9190758/mysql-default-date-14-days-for-a-column                                |
| SQLAlchemy Join문 예시  |https://stackoverflow.com/questions/27900018/flask-sqlalchemy-query-join-relational-tables                         |
| nginx sock error        |https://stackoverflow.com/questions/32974204/got-no-such-file-or-directory-error-while-configuring-nginx-and-uwsgi |

- nginx error log 확인: vim \var\log\nginx\error.log

## 프로젝트 환경 설정
```bash
1. OS : WSL2
- 세팅 방법 : https://www.44bits.io/ko/post/wsl2-install-and-basic-usage

2. 가상환경 설정

# venv
$ python3 -m venv .myenv

# venv start
$ source .myenv/bin/activate

# pip package 설치(.venv 진입상태)
$ pip install -r requirements.txt


3. 데이터베이스 설치 및 설정
- DB 버전 : 10.3.31-MariaDB-0ubuntu0.20.04.1
- Mariadb 진입 : sudo mysql -uroot -pmysql
- password 기입 : enter => password : pw => enter
- 데이터 베이스 생성 : create database <데이터베이스명>;

4. .env 파일 생성
DB_CONNECT=mysql+pymysql://<ID>:<PW>@127.0.0.1:3306/<데이터베이스명>
PW='<PW>'

5. flask db Migrate(.venv 진입상태)
& flask db init
& flask db migrate
& flask db upgrade

6. 트리거만 추가.(.venv 진입상태)
- 대여 시 자동으로 현재날짜와 반납일자를 데이터베이스에 넣어줍니다.
$ mysql -u<ID> -p<PW> <데이터베이스명> < sql/rent_trigger.sql

7. 테스트 데이터 넣어주기
$ insert/csv_insert.py 실행
$ insert/inventory_insert.py 실행

8. Flask run 설정
$ export FLASK_APP=app.py
$ flask run

```

### 서버 배포(nginx + uwsgi + flask)
```
1. 파이썬 개발환경 구축
$ sudo apt update  
$ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
$ sudo apt install python3-venv

2. 데이터 베이스 설치 및 설정
$ sudo apt-get install mysql-server
$ sudo systemctl enable mysql

$ sudo mysql -u root
$ use mysql;
$ update user set plugin='mysql_native_password' where user='root';
$ flush privileges;
$ alter user '<ID'@'localhost' IDENTIFIED BY'<PW>';
$ flush privileges;

$ create database <데이터베이스명>

3. 가상환경 진입
$ python3 -m venv .myenv

- venv start
$ source .myenv/bin/activate

4. pip package 설치(.venv 진입상태)
$ pip install -r requirements.txt
$ pip3 install flask flask-sqlalchemy pymysql Flask-Bcrypt uwsgi

5. .env 파일 설정
5-1 .env 파일 생성후 코드편집기로 해당 양식에 맞춰서 작성
DB_CONNECT=mysql+pymysql://<ID>:<PW>@127.0.0.1:3306/<데이터베이스명>
PW=<PW>

5-2 scp로 .env 파일 전송
- netstat -tnl 명령어를 통해 접근 가능한 포트의 설정여부 확인
- 열려있는 포트를 확인하고 해당 포트로 scp 명령어를 통한 파일전송

$ scp -p<열려있는 포트번호> <파일경로> <ID>@<도메인주소>:<저장할 디렉토리경로>
$ scp -p 3306 ./elice_backend/.env <ID>@<도메인주소>:test/elice_backend

6. flask db Migrate(.venv 진입상태)
& flask db init
& flask db migrate
& flask db upgrade


7. 트리거만 추가.(.venv 진입상태)
- 대여 시 자동으로 현재날짜와 반납일자를 데이터베이스에 넣어줍니다.
$ mysql -u<ID> -p<PW> <데이터베이스명> < sql/rent_trigger.sql

8. wsgi.py 생성 및 연결확인
        ==python==
from app import create_app

app = create_app()
if __name__ =="__main__":
    app.run()

- 연결 확인
uwsgi -–socket 0.0.0.0:5000 --protocol=http –w wsgi:app

9. ini 파일 설정. 
vim test.ini
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = test.ini
chmod-socket = 660
vacuum = true

die-on-term = true

10. uwsgi를 systemctl로 올리기
$ sudo vim /etc/systemd/system/test.service
[Unit]
Description=uWSGI instance to serve test
After=network.target

[Service]
User=<ID>
Group=www-data
WorkingDirectory=/home/<ID>/test
Environment="PATH=/home/<ID>/test/.myenv/bin"
ExecStart=/home/<ID>/test/.myenv/bin/uwsgi --ini test.ini

[Install]
WantedBy=multi-user.target

sudo systemctl start test
sudo systemctl enable test
sudo systemctl status test

11. Nginx 설치
$ sudo apt-get install nginx
$ sudo vim /etc/nginx/sites-available/default

- /etc/nginx/sites-available/default 변경할 부분
location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        #try_files $uri $uri/ =404;
        include uwsgi_params;
        uwsgi_pass unix:/home/<ID명>/test/test.sock;
}

12. Nginx 설정
- nginx 설정 확인
$ sudo nginx -t

- nginx 재적용
$ sudo systemctl restart nginx


13. 서비스 실행
- nginx 정지
$ sudo service ngnix stop

- sock 실행
$ uwsgi test.ini

- nginx 시작
$ sudo service nginx start
```
