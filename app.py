from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask import Flask
from db_connect import db
from flask_migrate import Migrate
from config import config

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) # config에서 가져온 파일 사용하기
    db.init_app(app) #SQLAlchemy 객체를 app객체와 이어줌.
    Migrate().init_app(app, db)

    from views import main_view, rent_view, comment_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(rent_view.bp)
    app.register_blueprint(comment_view.bp)

    app.secret_key = "secret"
    app.config['SESSION_TYPE'] = 'filesystem'

    return app
if __name__ == '__main__':
    create_app().run(debug=True)
