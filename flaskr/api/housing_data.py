from flask import Blueprint, request, jsonify
from flaskr.db import get_housing_data, get_regions
from flask_cors import CORS

housing_data = Blueprint('housing_data', 'housing_data', url_prefix='/housing_data')

CORS(housing_data)

@housing_data.route('/', methods=['GET'])
def api_housing_data():

    movies = get_housing_data()

    response = {
        "movies": movies
    }

    return jsonify(response)

@housing_data.route('/regions', methods=['GET'])
def api_regions():

    regions = get_regions()

    response = {
        "regions": regions
    }

    return jsonify(response)