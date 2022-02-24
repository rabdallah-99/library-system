from application import db
#this file to be modified to create the tables in the database

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    bdate = db.Column(Bdate)
    phone = db.Column(db.String(20))

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))

   #need to write the relations between tables
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    author_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)
  #need to write the relations between tables
class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    borrower_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    borrow_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    status = db.Column (db.String(5))



