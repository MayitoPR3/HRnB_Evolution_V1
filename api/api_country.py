#!/usr/bin/python3
# API to manage countries


from flask import request
from flask_restx import Namespace, Resource, fields
from datamanagment import DataManager
from model.country import Country

ns = Namespace('countries', description='Operations related to countries')
data_manager = DataManager()

country_model = ns.model('Country', {
    'country_code': fields.String(required=True, description='The ISO country code'),
    'name': fields.String(required=True, description='The name of the country'),
    'created_at': fields.DateTime(description='The creation date of the country record'),
    'updated_at': fields.DateTime(description='The date the country record was last updated')
})

@ns.route('/')
class Countries(Resource):
    @ns.marshal_list_with(country_model)
    def get(self):
        """Fetch all countries."""
        return data_manager.get_all_countries()

    @ns.expect(country_model)
    @ns.response(201, 'Country created successfully')
    def post(self):
        """Create a new country."""
        new_country = request.json
        country = Country(new_country['country_code'], new_country['name'])
        data_manager.save_country(country.to_dict())
        return {'message': 'Country created successfully', 'country_id': country.id}, 201

@ns.route('/<string:country_id>')
class CountryResource(Resource):
    @ns.marshal_with(country_model)
    @ns.response(404, 'Country not found')
    def get(self, country_id):
        """Fetch a country by its ID."""
        country = data_manager.get_country(country_id)
        if country:
            return country
        ns.abort(404, 'Country not found')

    @ns.response(204, 'Country deleted successfully')
    def delete(self, country_id):
        """Delete a country."""
        if data_manager.delete_country(country_id):
            return '', 204
        ns.abort(404, 'Country not found')

    @ns.expect(country_model)
    @ns.response(204, 'Country updated successfully')
    def put(self, country_id):
        """Update a country."""
        country_data = request.json
        country_data['country_id'] = country_id
        country_data['updated_at'] = datetime.now().isoformat()
        if data_manager.update_country(country_id, country_data):
            return '', 204
        ns.abort(404, 'Country not found')
