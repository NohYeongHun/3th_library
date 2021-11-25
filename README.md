# 도서관 대출 서비스


### 진행 사항

---
- **로그인**
    - 세션을 통한 로그인 유지
    - 비밀번호 규칙에 따른 비밀번호 기입
    - 아이디 규칙에 따른 아이디 기입(이메일)<br/>
    
- **회원가입**
    - 아이디, 비밀번호 기입을 통한 회원가입
    - 비밀번호와 아이디를 형식에 맞춰서 회원가입(개인정보 보호조치 준수)<br/>

- **로그아웃**
    - 세션을 통한 로그아웃<br/>

- **DB생성**
    - User 테이블 생성(사용자 정보)
    - Book 테이블 생성(책에 대한 정보)
    - Rent 테이블 생성(사용자의 대여 정보)
    - Comment 테이블 생성(책에 대한 평가 정보)
    - Inventory 테이블 생성(책의 재고에 대한 정보)<br/>

- **메인페이지**
    - 메인페이지 레이아웃 설정
    - 페이지 네이션 구현
    - 책의 평점 표기(반올림 구현)<br/>

- **상세페이지**
    - 댓글 작성 기능 구현
    - id 값에 맞는 정보 출력 구현
    - 댓글 목록 보여주기 구현<br/>


### ToDo-List
| 항목                    |내용                                | 진행 여부                                                               |
|:-----------------------:|:----------------------------------:|:-----------------------------------------------------------------------:|
|대여하기                 | DB 로직 구현                       | <ul><li> - [x] DB로직 구현</li>                                    </ul>|
|반납하기                 | 페이지 레이아웃 구현, DB 로직 구현 | <ul><li> - [x] DB로직 구현</li><li> - [x] 페이지 레이아웃 구현</li></ul>|
|대여기록                 | 페이지 레이아웃 구현, DB 로직 구현 | <ul><li> - [x] DB로직 구현</li><li> - [x] 페이지 레이아웃 구현</li></ul>|
|코드 정리                | 코드 정리하기(후 순위)             | <ul><li> - [ ]  ??</li><li> - [ ] ?? </li></ul>                         |


### 참조 사이트
|참조 내용                |참조 사이트                                                                                            |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------:|
|페이지네이션             |https://wikidocs.net/81054                                                                             |
|라디오 버튼              |https://stackoverflow.com/questions/15839169/how-to-get-value-of-selected-radio-button                 |
|플라스크와html간 변수전달|https://velog.io/@dltpal07/flask%EC%99%80-html-%EA%B0%84%EC%9D%98-%EB%B3%80%EC%88%98-%EC%A0%84%EB%8B%AC|
| 점수 아이콘 css         |https://www.codingnepalweb.com/star-rating-html-css-javascript/                                        |
| button href 사용 예시   |https://www.codestudyblog.com/sf2002e/0224200636.html                                                  |
| 패스워드 정규식         |https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/                     |
| MySQL 트리거            |https://stackoverflow.com/questions/9190758/mysql-default-date-14-days-for-a-column                    |
| SQLAlchemy Join문 예시  |https://stackoverflow.com/questions/27900018/flask-sqlalchemy-query-join-relational-tables             |