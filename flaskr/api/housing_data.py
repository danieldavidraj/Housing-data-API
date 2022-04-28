from flask_restx import Namespace, Resource, fields
from flaskr.db import (
    get_housing_data, 
    get_housing_data_with_id, 
    write_housing_data, 
    update_housing_data,
    delete_housing_data
)
from flask import jsonify

api = Namespace('housingData', description='Housing Data related operations')

resource_fields = api.model('Resource', {
    'name': fields.String,
    'place': fields.String
})

@api.route('/')
class HousingData(Resource):
    def get(self):
        housing_data = get_housing_data()
        return jsonify(housing_data)
    
    @api.expect(resource_fields, code=201)
    def post(self):
        document = api.payload
        return write_housing_data(document)

@api.route('/<id>')
class HousingDataItem(Resource):
    def get(self, id):
        housing_data = get_housing_data_with_id(id)
        return jsonify(housing_data)
    
    @api.expect(resource_fields, code=201)
    def put(self, id):
        data = api.payload
        return update_housing_data(id, data)
    
    def delete(self, id):
        return delete_housing_data(id)

    