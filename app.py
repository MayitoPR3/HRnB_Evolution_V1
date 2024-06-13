#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from api.api_country import ns as country_namespace
from api.api_city import ns as city_namespace
from api.api_amenities import ns as amenity_namespace
from api.api_places import ns as place_namespace
from api.api_review import ns as review_namespace
from api.usrmanagment import ns as user_namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API',
          description='A simple API for the HBnB application',
          )

# Add namespaces
api.add_namespace(country_namespace)
api.add_namespace(city_namespace)
api.add_namespace(amenity_namespace)
api.add_namespace(place_namespace)
api.add_namespace(review_namespace)
api.add_namespace(user_namespace)

if __name__ == '__main__':
    app.run(debug=True)
