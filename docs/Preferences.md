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

6. 테스트 데이터 넣어주기
$ insert/csv_insert.py 실행
$ insert/inventory_insert.py 실행

7. Flask run 설정
$ export FLASK_APP=app.py
$ flask run

```