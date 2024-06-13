#!/usr/bin/python3
"""API for managing amenities"""

from flask import request
from flask_restx import Namespace, Resource, fields
from datamanagment import DataManager
from model.amenities import Amenity
import uuid
from datetime import datetime

ns = Namespace('amenities', description='Operations related to amenities')
data_manager = DataManager()

# Model definition for an Amenity
amenity_model = ns.model('Amenity', {
    'id': fields.String(readOnly=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Amenity name'),
    'description': fields.String(required=False, description='Amenity description'),
    'created_at': fields.DateTime(readOnly=True, description='Date and time when the amenity was created'),
    'updated_at': fields.DateTime(readOnly=True, description='Date and time when the amenity was last updated')
})

@ns.route('/')
class AmenitiesResource(Resource):
    @ns.marshal_list_with(amenity_model)
    def get(self):
        """Fetch all amenities."""
        return data_manager.get_all_amenities()

    @ns.expect(amenity_model)
    @ns.response(201, 'Amenity created successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(409, 'Amenity name already exists')
    def post(self):
        """Create a new amenity."""
        new_amenity_data = request.json
        if data_manager.check_amenity_name_exists(new_amenity_data['name']):
            ns.abort(409, 'Amenity name already exists')
        new_amenity = Amenity(**new_amenity_data)
        data_manager.save_amenity(new_amenity.to_dict())
        return {'message': 'Amenity created successfully', 'amenity_id': new_amenity.id}, 201

@ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @ns.marshal_with(amenity_model)
    @ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Fetch an amenity by its ID."""
        amenity = data_manager.get_amenity(amenity_id)
        if amenity:
            return amenity
        ns.abort(404, 'Amenity not found')

    @ns.response(204, 'Amenity deleted successfully')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an existing amenity."""
        if not data_manager.delete_amenity(amenity_id):
            ns.abort(404, 'Amenity not found')
        return '', 204

    @ns.expect(amenity_model)
    @ns.response(204, 'Amenity updated successfully')
    @ns.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an existing amenity."""
        amenity = data_manager.get_amenity(amenity_id)
        if not amenity:
            ns.abort(404, 'Amenity not found')
        data_manager.update_amenity(amenity_id, request.json)
        return '', 204
