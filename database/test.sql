CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE category(
category_id int NOT NULL AUTO_INCREMENT,
category_name varchar(40),
PRIMARY KEY(category_id)
);

CREATE TABLE author(
author_id int NOT NULL AUTO_INCREMENT,
author_name varchar(50) NOT NULL,
PRIMARY KEY(author_id )
);

CREATE TABLE books(
book_id int NOT NULL AUTO_INCREMENT,
book_name varchar(40) NOT NULL,
author_id int NOT NULL,
category_id int NOT NULL,
price decimal(6,2) ,
count int,
available TINYINT,
PRIMARY KEY(book_id),
FOREIGN KEY (author_id) REFERENCES author(author_id),
FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE login(
user_id int NOT NULL AUTO_INCREMENT,
user_name varchar(50) NOT NULL,
password varchar(50),
PRIMARY KEY(user_id)
);

CREATE TABLE borrower(
borrower_id int NOT NULL AUTO_INCREMENT,
borrower_name varchar(50) NOT NULL,
borrower_address varchar(50) ,
borrower_bdate DATE,
borrower_phone varchar(20),
PRIMARY KEY(borrower_id)
);

CREATE TABLE transaction(
transaction_id int NOT NULL AUTO_INCREMENT,
borrower_id int NOT NULL ,
book_id int NOT NULL ,
borrow_date DATE,
return_date DATE,
status varchar(5),
PRIMARY KEY(transaction_id),
FOREIGN KEY (book_id) REFERENCES books(book_id),
FOREIGN KEY (borrower_id) REFERENCES borrower(borrower_id)
);




