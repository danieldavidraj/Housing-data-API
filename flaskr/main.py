import os
import configparser
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from bson import json_util, ObjectId
from datetime import datetime
from flaskr.api.housing_data import housing_data

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
app.json_encoder = MongoJsonEncoder
app.register_blueprint(housing_data)

app.config['MONGO_URI'] = config['PROD']['DB_URI']

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return 'Hello, World!'