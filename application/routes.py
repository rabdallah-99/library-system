from flask import render_template
from application import app, db, conn, mysql
from application.forms import *
from application.models import Category, Author, Borrower, Books, Transaction


@app.route('/category', methods=['GET', 'POST'])
def add_category():
    form = AddCategory()
    if form.validate_on_submit():
        new_category = Category(category_id=0, category_name=form.name.data)
        db.session.add(new_category)
        db.session.commit()
    return render_template('Category.html', title='Category', form=form)


@app.route('/author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthor()
    if form.validate_on_submit():
        new_author = Author(author_id=0, author_name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
    else:
        print(form.errors)
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
        new_book = Books(book_id=0, book_name=form.book_name.data, author_id=form.author_id.data, category_id=form.category_id.data, price=form.price.data, count=form.count.data)
        db.session.add(new_book)
        db.session.commit()
    else:
        print(form.errors)
    return render_template("book.html", joblist=joblist, joblist1=joblist1, form=form)


@app.route('/borrower', methods=['GET', 'POST'])
def addBorrower():
    form = AddBorrower()
    if form.validate_on_submit():
        new_borrower = Borrower(borrower_id=0, borrower_name=form.borrower_name.data, borrower_address=form.borrower_address.data, borrower_bdate=form.borrower_bdate.data, borrower_phone=form.borrower_phone.data)
        db.session.add(new_borrower)
        db.session.commit()
    else:
        print(form.errors)
    return render_template('borrower.html', title='borrower', form=form)


@app.route('/transaction', methods=['GET', 'POST'])
def borrowbook():
    form = AddTransaction()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT borrower_id,borrower_name FROM borrower')
    joblist = cursor.fetchall()
    form.borrower_id.choices = [(h[0], h[1]) for h in joblist]
    cursor.execute('SELECT book_id,book_name FROM books WHERE count > 0')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    form.status.choices = [('O', 'OUT'), ('L', 'Late'), ('R', 'Returned')]
    if form.validate_on_submit():
        new_transaction = Transaction(transaction_id=0, borrower_id=form.borrower_id.data, book_id=form.book_id.data, borrow_date=form.borrow_date.data, return_date=form.return_date.data, status=form.status.data)
        db.session.add(new_transaction)
        book1 = Books.query.filter_by(book_id=form.book_id.data).first()
        Books.query.filter_by(book_id=form.book_id.data).update(dict(count=book1.count-1))
        db.session.commit()
    else:
        print(form.errors)
    return render_template("transaction.html", joblist=joblist, joblist1=joblist1, form=form)


@app.route('/read')
def readcategory():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category')
    all_category = cursor.fetchall()
    headings = ("ID", " Name")
    return render_template('display.html', title='Category', data=all_category, headings=headings)


@app.route('/read-author')
def readauthor():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM author')
    all_authors = cursor.fetchall()
    headings = ("ID", " Name")
    return render_template('display.html', title='Authors', data=all_authors, headings=headings)


@app.route('/read-borrower')
def readborrower():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM borrower')
    all_books = cursor.fetchall()
    headings = ("ID", " Name", "Address", "birth date", "phone")
    return render_template('display.html', title='Borrower', data=all_books, headings=headings)


@app.route('/read-book')
def readbook():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vbook')
    all_books = cursor.fetchall()
    headings = ("ID", "Book Name", "Author id", "Category id", "price", "count")
    conn.commit()
    return render_template('display.html', title='Books', data=all_books, headings=headings)


@app.route('/readtransaction')
def readtransaction():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM borrowbook')
    all_transaction = cursor.fetchall()
    headings = ("ID", "Borrower", "Book", "Borrow date", "Return date", "status")
    return render_template('display.html', title='transactions', data=all_transaction, headings=headings)

# Route to home page


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title='Home')

# Route to about page


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/deletecategory', methods=['GET', 'POST'])
def delete_category():
    form = DeleteCategory()
    cursor = conn.cursor()
    cursor.execute('SELECT category_id,category_name FROM category')
    joblist1 = cursor.fetchall()
    form.category_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Category.query.filter_by(category_id=form.category_id.data).delete()
        db.session.commit()
    return render_template("delcat.html", joblist1=joblist1, form=form)


@app.route('/deleteauthor', methods=['GET', 'POST'])
def delete_author():
    form = DeleteAuthor()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM author')
    joblist1 = cursor.fetchall()
    form.author_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Author.query.filter_by(author_id=form.author_id.data).delete()
        db.session.commit()
    return render_template("delauth.html", joblist1=joblist1, form=form)


@app.route('/deletebook', methods=['GET', 'POST'])
def delete_book():
    form = DeleteBook()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT book_id,book_name FROM books')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Books.query.filter_by(book_id=form.book_id.data).delete()
        db.session.commit()
    return render_template("delbook.html", joblist1=joblist1, form=form)


@app.route('/deleteborrower', methods=['GET', 'POST'])
def delete_borrower():
    form = DeleteBorrower()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT borrower_id,borrower_name FROM borrower')
    joblist1 = cursor.fetchall()
    form.borrower_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Borrower.query.filter_by(borrower_id=form.borrower_id.data).delete()
        db.session.commit()
    return render_template("delborrower.html", joblist1=joblist1, form=form)


@app.route('/updatecategory', methods=['GET', 'POST'])
def update_category():
    form = UpdateCategory()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT category_id,category_name FROM category')
    joblist1 = cursor.fetchall()
    form.category_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Category.query.filter_by(category_id=form.category_id.data).update(dict(category_name=form.category_name.data))
        db.session.commit()
    return render_template("modcat.html", joblist1=joblist1, form=form)


@app.route('/updateauthor', methods=['GET', 'POST'])
def update_author():
    form = UpdateAuthor()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT author_id,author_name FROM author')
    joblist1 = cursor.fetchall()
    form.author_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Author.query.filter_by(author_id=form.author_id.data).update(dict(author_name=form.author_name.data))
        db.session.commit()
        conn.close()
    return render_template("modauth.html", joblist1=joblist1, form=form)


@app.route('/updatebook', methods=['GET', 'POST'])
def update_book():
    form = UpdateBook()
    cursor = conn.cursor()
    cursor.execute('SELECT book_id,book_name FROM books')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Books.query.filter_by(book_id=form.book_id.data).update(dict(count=form.count.data))
        Books.query.filter_by(book_id=form.book_id.data).update(dict(price=form.price.data))
        db.session.commit()
    return render_template("modbook.html", joblist1=joblist1, form=form)


@app.route('/updateborrower', methods=['GET', 'POST'])
def update_borrower():
    form = UpdateBorrower()
    cursor = conn.cursor()
    cursor.execute('SELECT borrower_id,borrower_name FROM borrower')
    joblist1 = cursor.fetchall()
    form.borrower_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Borrower.query.filter_by(borrower_id=form.borrower_id.data).update(dict(borrower_address=form.borrower_address.data))
        Borrower.query.filter_by(borrower_id=form.borrower_id.data).update(dict(borrower_bdate=form.borrower_bdate.data))
        Borrower.query.filter_by(borrower_id=form.borrower_id.data).update(dict(borrower_phone=form.borrower_phone.data))
        db.session.commit()
    return render_template("modborrower.html", joblist1=joblist1, form=form)


@app.route('/changebookprice', methods=['GET', 'POST'])
def changeprice():
    form = UpdatePrice()
    cursor = conn.cursor()
    cursor.execute('SELECT book_id,book_name FROM books')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Books.query.filter_by(book_id=form.book_id.data).update(dict(price=form.price.data))
        db.session.commit()
    return render_template("modprice.html", joblist1=joblist1, form=form)


@app.route('/changebookcount', methods=['GET', 'POST'])
def changecount():
    form = UpdateCount()
    cursor = conn.cursor()
    cursor.execute('SELECT book_id,book_name FROM books')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    if form.validate_on_submit():
        Books.query.filter_by(book_id=form.book_id.data).update(dict(count=form.count.data))
        db.session.commit()
    return render_template("modcount.html", joblist1=joblist1, form=form)


@app.route('/returnbook', methods=['GET', 'POST'])
def returnbook():
    form = ReturnBook()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT borrower_id,borrower_name FROM borrower')
    joblist = cursor.fetchall()
    form.borrower_id.choices = [(h[0], h[1]) for h in joblist]
    cursor.execute('SELECT book_id,book_name FROM books ')
    joblist1 = cursor.fetchall()
    form.book_id.choices = [(h[0], h[1]) for h in joblist1]
    form.status.choices = [('O', 'OUT'), ('L', 'Late'), ('R', 'Returned')]
    if form.validate_on_submit():
        tr = Transaction.query.filter_by(book_id=form.book_id.data, borrower_id=form.borrower_id.data, status='O' ).first()
        Transaction.query.filter_by(transaction_id=tr.transaction_id).update(dict(status='R'))
        db.session.commit()
        book1 = Books.query.filter_by(book_id=form.book_id.data).first()
        Books.query.filter_by(book_id=form.book_id.data).update(dict(count=book1.count+1))
        db.session.commit()
    else:
        print(form.errors)
    return render_template("transaction1.html", joblist=joblist, joblist1=joblist1, form=form)


@app.route('/findlate', methods=['GET', 'POST'])
def searchlate():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM borrowbook   WHERE borrow_date +7 < CURDATE()  AND status= 'O'")
    all_authors = cursor.fetchall()
    headings = ("ID", "Borrower", "Book", "Borrow date", "Return date", "status")
    return render_template('display.html', title='Authors', data=all_authors, headings=headings)
