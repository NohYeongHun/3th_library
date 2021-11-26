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
|참고 내용                |참조 사이트                                                                                            |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------:|
|페이지네이션             |https://wikidocs.net/81054                                                                             |
|라디오 버튼              |https://stackoverflow.com/questions/15839169/how-to-get-value-of-selected-radio-button                 |
|플라스크와html간 변수전달|https://velog.io/@dltpal07/flask%EC%99%80-html-%EA%B0%84%EC%9D%98-%EB%B3%80%EC%88%98-%EC%A0%84%EB%8B%AC|
| 점수 아이콘 css         |https://www.codingnepalweb.com/star-rating-html-css-javascript/                                        |
| button href 사용 예시   |https://www.codestudyblog.com/sf2002e/0224200636.html                                                  |
| 패스워드 정규식         |https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/                     |
| MySQL 트리거            |https://stackoverflow.com/questions/9190758/mysql-default-date-14-days-for-a-column                    |
| SQLAlchemy Join문 예시  |https://stackoverflow.com/questions/27900018/flask-sqlalchemy-query-join-relational-tables             |



## 프로젝트 환경 설정
```bash
1. OS : WSL2
- 세팅 방법 : https://www.44bits.io/ko/post/wsl2-install-and-basic-usage

2. 가상환경 설정

# venv
$ python -m venv .myenv

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


