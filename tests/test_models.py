from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import Category, Author, Borrower, Books, Transaction
from datetime import date, datetime

# Create the base class


class TestBase(TestCase):
    def create_app(self):
        config_name = "Testing"

        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://riham:root@127.0.0.1/test', SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()
        sample10 = Category(category_id=13, category_name="fiction")
        sample20 = Author(author_id=6, author_name="J K Rollings")
        sample4 = Books(book_id=53, book_name="harry potter", author_id=6, category_id=13, price=15, count=10)
        bdate = date(2012, 12, 4).isoformat()
        sample1 = Borrower(borrower_id=1, borrower_name="Mona", borrower_address="123 burton road", borrower_bdate=bdate, borrower_phone="532665")
        # save category to database
        db.session.add(sample20)
        db.session.add(sample10)
        db.session.add(sample1)
        db.session.commit()
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
        book1 = Books.query.filter_by(book_id=53).first()
        cat = Category.query.filter_by(category_id=13).first()
        mona = Borrower.query.filter_by(borrower_name="Mona").first()
        assert book1.book_id == 53
        assert book1.book_name == "harry potter"
        assert book1.price == 15
        assert cat.category_name == "fiction"
        tr1 = Transaction(transaction_id=1, borrower_id=mona.borrower_id, book_id=book1.book_id, borrow_date=datetime.today(), return_date="2022-03-12", status='O')
        assert tr1.borrower_id == mona.borrower_id


class TestRoutes (TestBase):
    def test_route(self):
        response = self.client.get(url_for('readauthor'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('readborrower'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('addtransaction'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('delete_category'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('update_book'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('update_category'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('delete_borrower'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('delete_author'))
        self.assertEqual(response.status_code, 200)




