from flask import Flask, render_template, request
from application import app, db
from application.forms import AddCategory, AddAuthor, LogInForm, SignUpForm
from application.models import Category, Author, Borrower, Login, Books
#modify this file to suit your database and site layout
@app.route('/category', methods=['GET', 'POST'])
def add_category():
    form=AddCategory()
    if form.validate_on_submit():
        new_category = Category (category_id=0, category_name = form.name.data)
        db.session.add(new_category)
        db.session.commit()
    return render_template('Category.html', title='Category', form = form)
@app.route('/deletecategory',methods=['GET','POST'])
def delete_category():
    form=DeleteCategory()

@app.route('/author', methods=['GET', 'POST'])
def add_author():
    form=AddAuthor()
    if form.validate_on_submit():
        new_author = Author(author_id=0, author_name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
    return render_template('author.html', title='Author', form = form)

@app.route('/read')
def readcategory():

    all_category = Category.query.all()
    category_string = ""
    for category in all_category:
        category_string += "<br>"+ category.category_name
    return category_string
@app.route('/read-author')
def readauthor():

    all_authors = Author.query.all()
    author_string = ""
    for author in all_authors:
        author_string += "<br>"+ author.author_name
    return  author_string
# Route to home page
@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title = 'Home')

# Route to about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')
