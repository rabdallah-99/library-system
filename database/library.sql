CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE category(
category_id int NOT NULL AUTO,
categoy_name varchar(40)
):
CREATE TABLE books(
book_id int NOT NULL AUTO_INCREMENT,
book_name varchar(40) NOT NULL,
publisher_id int NOT NULL,
category_id int NOT NULL,
PRIMARY KEY(book_id),
FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

CREATE TABLE publishers(
publisher_id int NOT NULL AUTO_INCREMENT,
publisher_name varchar(40) NOT NULL,
publisher_email varchar (40),
publisher_address varchar (60),
PRIMARY KEY(publisher_id )
);
