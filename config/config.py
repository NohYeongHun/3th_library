from dotenv import load_dotenv
import os

# dotenv 사용
load_dotenv()
DB_CONNECT = os.environ.get("DB_CONNECT")

SQLALCHEMY_DATABASE_URI = DB_CONNECT
SQLALCHEMY_TRACK_MODIFICATIONS = False