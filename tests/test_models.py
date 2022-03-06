from flask_testing import TestCase
from application import app, db
from application.models import Category, Author, Borrower, Books, Transaction

# Create the base class


class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app


    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality


class TestModel(TestBase):
    def test_models(self):

        sample10 = Category(category_id=13, category_name="fiction")
        sample20 = Author(author_id=26, author_name="J K Rollings")
        sample4 = Books(book_id=53, book_name="harry potter", author_id=26, category_id=13, price=15, count=10)
        # save category to database
        db.session.add(sample20)
        db.session.add(sample10)
        db.session.add(sample4)
        db.session.commit()
        book1 = Books.query.filter_by(book_id=53).first()
        assert book1.book_id == 53
        assert book1.book_name == "harry potter"
        assert book1.price == 15
        cat = Category.query.filter_by(category_id=13).first()
        assert cat.category_name == "fiction"



