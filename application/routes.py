from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.models import Category, Author, Borrower, login, Books
#modify this file to suit your database and site layout
@app.route('/category')
def add_category():
    new_category = Games(name="New Game")
    db.session.add(new_category)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/count')
def count():
	number_of_games = Games.query.count()
	return str(number_of_games)
@app.route('/delete')
def delete():
	game_to_delete = Games.query.first()
	db.session.delete(game_to_delete)
	db.session.commit()	
	return "Game deleted"
