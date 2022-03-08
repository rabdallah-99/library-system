from application import db
from datetime import datetime
#this file to be modified to create the tables in the database


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), nullable=False)
    def __repr__(self):
        return f" Category id : {self.category_id}     Category name = {self.category_name}"
    def getcategory(self,id1):
        statement = 'SELECT category_name FROM category WHERE category_id=' + id1
        self.category_name = db.Query.execute(statement)
        return self
    def updatecategory(self,id1,name):
        statement = "UPDATE category SET category_name=" + name + "WHERE category_id=" + id1
        db.Query.execute(statement)
        return "category updated"


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)

    def getauthor(self, d1):
        statement = 'SELECT author_name FROM author WHERE author_id=' + id1
        self.author_name = db.Query.execute(statement)
        return self

    def updateauthor(self, id1, name):
        statement = "UPDATE author SET author_name=" + name + "WHERE author_id=" + id1
        db.Query.execute(statement)
        return "author updated"

    
class Borrower(db.Model):
    borrower_id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String(50),nullable=False)
    borrower_address = db.Column(db.String(50),nullable=False)
    borrower_bdate = db.Column(db.DateTime)
    borrower_phone = db.Column(db.String(20))


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



