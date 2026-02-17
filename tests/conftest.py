import pytest
from app import app as flask_app

@pytest.fixture()
def app():
    # Put the app in testing mode
    flask_app.config.update({"TESTING": True})
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()