from application import db
from datetime import datetime
#this file to be modified to create the tables in the database


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), nullable=False)


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)


class Borrower(db.Model):
    borrower_id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String(50), nullable=False)
    borrower_address = db.Column(db.String(50), nullable=False)
    borrower_bdate = db.Column(db.DateTime)
    borrower_phone = db.Column(db.String(20))


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(40), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(Author.author_id))
    category_id = db.Column(db.Integer, db.ForeignKey(Category.category_id))
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)


class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey(Borrower.borrower_id), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(Category.category_id), nullable=False)
    borrow_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(5))



