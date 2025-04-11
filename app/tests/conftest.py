from pymongo import MongoClient
from app.settings import APP_SETTINGS
from fastapi.testclient import TestClient
from app import create_app
import pytest

@pytest.fixture(scope="session")
def test_db():
    """Setup test database and clean up afterwards"""
    client = MongoClient(APP_SETTINGS.MONGO_DB_ATLAS_URI)
    db = client[APP_SETTINGS.USERS_DB_NAME + "_test"]
    
    return db


@pytest.fixture(scope="session")
def app(test_db):
    """Create FastAPI app with test database"""
    app = create_app()
    
    # Override the database connection
    app.database = test_db
    
    return app

@pytest.fixture(scope="session")
def client(app):
    """Create TestClient for the app"""
    return TestClient(app)

from app.tests.fixture.auth import *