import pymysql
from flask import Flask
from db_connect import db
from dotenv import load_dotenv
import os

app = Flask(__name__)

# dotenv 사용
load_dotenv()
DB_CONNECT = os.environ.get("DB_CONNECT")

# DB 연결
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECT
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
# hello