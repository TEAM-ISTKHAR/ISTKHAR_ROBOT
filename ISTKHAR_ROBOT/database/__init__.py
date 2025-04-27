

from async_pymongo import AsyncClient

from ISTKHAR_ROBOT import MONGO_DB_URI

DBNAME = "ISTKHAR_ROBOT"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
