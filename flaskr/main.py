import os
import configparser
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from bson import json_util, ObjectId
from datetime import datetime
from flask_restx import Api
from flaskr.api.housing_data import api as ns1

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = config['PROD']['DB_URI']

app.json_encoder = MongoJsonEncoder

api = Api(
    app, 
    version='1.0', 
    title='Housing Data',
    description='A simple Housing Data API'
)

api.add_namespace(ns1)

