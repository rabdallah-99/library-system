from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Category, Author, Borrower, Books, Transaction

# Create the base class


class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test
        sample1 = Category(category_id=4, category_name="comedy")
        sample10 = Category(category_id=5, category_name="fiction")
        sample2 = Author(author_id=4, author_name="William Wordsworth")
        sample20 = Author(author_id=6, author_name="J K Rollings")
        #sample3 = Borrower(borrower_id=5, borrower_name="test user", borrower_bdate="05/03/1980", borrower_phone="078954321")
        sample4 = Books(book_id=3, book_name="harry potter", author_id=6, category_id=5, price=15, count=10)
        # save category to database
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.add(sample10)
        db.session.add(sample4)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestModel(TestBase):
    def test_models(self):

	    self.assertEqual( sample1.category_name ,"comedy")
	#assert TestBase.sample3.borrower_id == 5
	#assert TestBase.sample20.author_id == 6


