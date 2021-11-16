create table book(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    book_name varchar(256) NOT NULL,
    publisher varchar(20) NOT NULL,
    author varchar(20) NOT NULL,
    publication_date DATETIME,
    pages INT NOT NULL,
    isbn long NOT NULL,
    description varchar(2000) NOT NULL,
    link varchar(200) NOT NULL
);