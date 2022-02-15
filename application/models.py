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

class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
   
#class Books(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(40))
#    price = db.Column(db.Integer)

