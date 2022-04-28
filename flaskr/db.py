from flask_pymongo import PyMongo
from flask import current_app, g
from werkzeug.local import LocalProxy
from bson.objectid import ObjectId

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
    housing_data = db.HousingData.find({}).limit(10)
    return list(housing_data)

def get_housing_data_with_id(id):
    housing_data = db.HousingData.find({"_id": ObjectId(id)})
    return list(housing_data)

def write_housing_data(new_document):
    response = db.HousingData.insert_one(new_document)
    output = {'Status': 'Successfully Inserted',
              'Document_ID': str(response.inserted_id)}
    return output

def update_housing_data(id, data):
    filt = {"_id": ObjectId(id)}
    updated_data = {"$set": data}
    response = db.HousingData.update_one(filt, updated_data)
    output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
    return output

def delete_housing_data(id):
    filt = {"_id": ObjectId(id)}
    response = db.HousingData.delete_one(filt)
    output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
    return output