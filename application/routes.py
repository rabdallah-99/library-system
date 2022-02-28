from flask import Flask, render_template, request
from application import app, db, conn
from application.forms import AddCategory, AddAuthor, LogInForm, SignUpForm, AddBook, AddBorrower
from application.models import Category, Author, Borrower, Login, Books
import datetime
#modify this file to suit your database and site layout


@app.route('/category', methods=['GET', 'POST'])
def add_category():
    form = AddCategory()
    if form.validate_on_submit():
        new_category = Category(category_id=0, category_name=form.name.data)
        db.session.add(new_category)
        db.session.commit()
    return render_template('Category.html', title='Category', form=form)
#@app.route('/deletecategory',methods=['GET','POST'])
#def delete_category():
#   form=DeleteCategory()


@app.route('/author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthor()
    if form.validate_on_submit():
        new_author = Author(author_id=0, author_name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
    return render_template('author.html', title='Author', form=form)


@app.route('/book', methods=['GET', 'POST'])
def addbook():
    form = AddBook()
    cursor = conn.cursor()
    cursor.execute('SELECT author_id,author_name FROM author')
    joblist = cursor.fetchall()
    form.author_id.choices = [(h[0], h[1]) for h in joblist]
    cursor.execute('SELECT category_id,category_name FROM category')
    joblist1 = cursor.fetchall()
    form.category_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        #return '<html><h1> {} </h1></html>'.format(form.author_id.data)
        id=db.Query('SELECT author_id FROM author WHERE author_name ='+form.author_id.data)
        category=db.Query('SELECT category_id FROM category WHERE category_name='+form.category_id.data)
        new_book = Books(book_id=0, book_name=form.book_name.data, author_id=id, category_id=category, price=form.price.data, count=form.count.data)
        db.session.add(new_book)
        db.session.commit()

    return render_template("book.html", joblist=joblist, joblist1=joblist1, form=form)

@app.route('/borrower', methods=['GET', 'POST'])
def addBorrower():
    form = AddBorrower()
    if form.validate_on_submit():
        new_borrower = Borrower(borrower_id=0, borrower_name=form.borrower_name.data, borrower_address=form.borrower_address.data, borrower_bdate=form.borrower_bdate.data, borrower_phone=form.borrower_phone.data)
        db.session.add(new_borrower)
        db.session.commit()
    return render_template('borrower.html', title='borrower', form=form)


@app.route('/read')
def readcategory():

    all_category = Category.query.all()
    category_string = ""
    for category in all_category:
        category_string += "<br>" + category.category_name
    return category_string


@app.route('/read-author')
def readauthor():

    all_authors = Author.query.all()
    author_string = ""
    for author in all_authors:
        author_string += "<br>"\
                         + author.author_name
    return author_string


@app.route('/read-borrower')
def readborrower():
    all_borrowers = Borrower.query.all()
    borrower_string = ""
    for borrower in all_borrowers:
        borrower_string += "<br>" + borrower.borrower_name +"\t"+ borrower.borrower_address +"\t"+ borrower.borrower_bdate.strftime("%m%d%Y") +"\t"+ borrower.borrower_phone
    return  borrower_string

@app.route('/read-book')
def readbook():
    all_books = Books.query.all()
    book_string = ""
    for book in all_books:
        book_string += "<br>" + book.book_name +"\t"+ book.author_id +"\t"+ book.category_id +"\t"+ book.price + "\t" + book.count
    return  book_string
# Route to home page


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title='Home')

# Route to about page


@app.route('/about')
def about():
    return render_template('about.html', title='About')
