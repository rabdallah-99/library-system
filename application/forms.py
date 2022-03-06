from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db, conn,mysql
from application.models import Borrower, Books, Author, Category, Transaction

# this file should build the available forms needed for project


class AddCategory(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add Category')


class AddAuthor(FlaskForm):
    name = StringField('Author Name', validators=[DataRequired()])
    submit = SubmitField('Add Author')


class AddBorrower(FlaskForm):
    borrower_name = StringField('Borrower Name', validators=[DataRequired()])
    borrower_address = StringField('Borrower Address', validators=[DataRequired()])
    borrower_bdate = DateField('Birthday date',format='%Y-%m-%d')
    borrower_phone = StringField('Borrower phone')
    submit = SubmitField('Add Borrower')


class AddBook(FlaskForm):

    book_name = StringField('Book Name', validators=[DataRequired()])
    author_id = SelectField('Author', coerce=int)
    category_id = SelectField('Category', coerce=int)
    price = FloatField('Book Price')
    count = IntegerField('Book Count')
    submit = SubmitField('Add Book')

class AddTransaction(FlaskForm):
    borrower_id = SelectField('Borrower Name', coerce=int)
    book_id = SelectField('Book Name', coerce=int)
    borrow_date = DateField('Borrowing date',format='%Y-%m-%d')
    return_date = DateField('Return date',format='%Y-%m-%d')
    status = SelectField('status')
    submit = SubmitField('Add Transaction')

class DeleteCategory(FlaskForm) :
    category_id = SelectField('Category Name', coerce=int)
    submit = SubmitField('Delete')

class DeleteAuthor(FlaskForm) :
    author_id = SelectField('Author Name', coerce=int)
    submit = SubmitField('Delete')

class DeleteBook(FlaskForm) :
    book_id = SelectField('Book Name', coerce=int)
    submit = SubmitField('Delete')

class DeleteBorrower(FlaskForm) :
    borrower_id = SelectField('borrower Name', coerce=int)
    submit = SubmitField('Delete')

class UpdateCategory(FlaskForm):
    category_id = SelectField('Category Name', coerce=int)
    category_name = StringField('New Name', validators=[DataRequired()])
    submit = SubmitField('Update')

class UpdateAuthor(FlaskForm):
    author_id = SelectField('Author Name', coerce=int)
    author_name = StringField('New Name', validators=[DataRequired()])
    submit = SubmitField('Update')

class UpdateBorrower(FlaskForm):
    borrower_id = SelectField('Borrower Name', coerce=int)
    borrower_address = StringField('Borrower address')
    borrower_bdate = DateField('Birthday date',format='%Y-%m-%d')
    borrower_phone = StringField('Borrower phone')
    submit = SubmitField('Update')

class UpdateBook(FlaskForm):
    book_id = SelectField('Book Name', coerce=int)
    price = FloatField('Book Price')
    count = IntegerField('Book Count')
    submit = SubmitField('Update')

class UpdatePrice(FlaskForm):
    book_id = SelectField('Book Name', coerce=int)
    price = FloatField('Book Price')
    submit = SubmitField('Update')

class UpdateCount(FlaskForm):
    book_id = SelectField('Book Name', coerce=int)
    count = IntegerField('Book Count')
    submit = SubmitField('Update')
#
#class UpdateTransaction(FlaskForm):
#    borrower_id = SelectField('Borrower Name', coerce=int)
#    book_id = SelectField('Book Name', coerce=int)
#    borrow_date = DateField('Borrowing date',format='%Y-%m-%d')
 #   return_date = DateField('Return date',format='%Y-%m-%d')
  #  status = SelectField('status')
   # submit = SubmitField('Add Transaction')
