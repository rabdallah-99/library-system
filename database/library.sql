CREATE DATABASE IF NOT EXISTS library;
USE library;
CREATE TABLE books(
book_id int NOT NULL AUTO_INCREMENT,
book_name varchar(40) NOT NULL,

PRIMARY KEY(book_id)
);
