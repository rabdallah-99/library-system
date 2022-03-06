import pytest
from application import app, db
from application.routes import *
from test_models import *

class TestRoutes(TestBase):

    def test_route(self):
        x = client.get("/")
        html = x.data.decode()
        assert "<a href=\"/home/\">Home</a>" in html

@pytest.fixture()
def client():
    client = app.test_client()
    yield client

    def test_route(self):
        x = client.get("/")
        html = x.data.decode()
        assert "<a href=\"/home/\">Home</a>" in html
