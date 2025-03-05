#from .. import create_app

from faker import Faker
import pytest



@pytest.fixture
def app():
    app = create_app(is_test_mode=True)
    return app