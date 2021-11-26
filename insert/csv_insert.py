import csv
import pymysql
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
pw = os.environ.get("PW")
conn = pymysql.connect(host='localhost', user='root', password=pw,
                       db='elice_library', charset='utf8')

curs = conn.cursor()
conn.commit()

with open('elice_library.csv','r') as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        book_name = row[1]
        publisher = row[2]
        author = row[3]
        publication_date = dt.datetime.strptime(row[4],"%Y-%m-%d")
        pages = row[5]
        isbn = row[6]
        description = row[7]
        link = row[8]
        sql = 'INSERT INTO book(book_name,publisher,author,publication_date,pages,isbn,description,link) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        curs.execute(sql,(book_name,publisher,author,publication_date,pages,isbn,description,link))
        
conn.commit()
f.close()
conn.close()