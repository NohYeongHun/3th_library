import pymysql
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
pw = os.environ.get("PW")
conn = pymysql.connect(host='localhost', user='root', password=pw, db='elice_library', charset='utf8')

curs = conn.cursor()
conn.commit()

for book_id in range(1,33):
    for value in range(1,4):
        sql = 'INSERT INTO inventory(book_id) VALUES(%s)'
        curs.execute(sql,(book_id))
        
conn.commit()
conn.close()