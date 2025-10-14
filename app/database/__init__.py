from pymongo import MongoClient, server_api
from app.settings import APP_SETTINGS

_client = None
_db = None

def get_database():
    global _client, _db
    if _db is None:
      
        _client = MongoClient(
            APP_SETTINGS.MONGO_DB_ATLAS_URI,
            server_api=server_api.ServerApi(version="1", strict=True, deprecation_errors=True)
        )
        _db = _client[APP_SETTINGS.DB_NAME]
    return _db