from flask_pymongo import PyMongo

from flask import current_app, g
from werkzeug.local import LocalProxy

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db

    return db

db = LocalProxy(get_db)

def get_housing_data():

    housing_data = db.HousingData.distinct({},{"region_id":1})

    return list(housing_data)

def get_regions():

    regions = db.HousingData.distinct({"region_id"}, {"region_name": 1,"_id":0}).limit(10)

    return list(regions)
