from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#from wtforms.fields.html5 import DateField
from application import db, bcrypt, conn
from application.models import Borrower, Books, Author, Category, Transaction, Login
#from flask_login import current_user
# this file should build the available forms needed for project


class LogInForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_user(self, name, password):
        user = Login.query.filter_by(name=name.data).first()

        if user is None:
            raise ValidationError('Unknown user name')

        if bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Incorrect password')

# Class for signing up


class SignUpForm(FlaskForm):
    user = StringField('User Name', validators=[DataRequired(), Length(min=3, max=15)])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


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
    author_id = SelectField('borrower Name', coerce=int)
    submit = SubmitField('Delete')