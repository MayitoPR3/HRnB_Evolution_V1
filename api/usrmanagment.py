#!/bin/usr/python3
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Conflict
import uuid
import re
from flask_restx import Namespace

ns = Namespace('users', description='User management operations')

app = Flask(__name__)

# Sample persistence layer 
users = {}

# Validation for email
email_regex = r'^\S+@\S+\.\S+$'


def validate_email(email):
    if not re.match(email_regex, email):
        raise BadRequest('Invalid email format')


def validate_name(name):
    if not name.strip():
        raise BadRequest('Name cannot be empty')


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not first_name or not last_name:
        raise BadRequest('Missing required fields')

    validate_email(email)
    validate_name(first_name)
    validate_name(last_name)

    if email in [user['email'] for user in users.values()]:
        raise Conflict('Email already exists')

    user_id = str(uuid.uuid4())
    user = {
        'id': user_id,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now())
    }
    users[user_id] = user
    return jsonify(user), 201


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFound('User not found')
    return jsonify(user)


@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFound('User not found')

    data = request.json
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if email and email != user['email'] and email in [u['email'] for u in users.values()]:
        raise Conflict('Email already exists')

    if email:
        validate_email(email)
        user['email'] = email
    if first_name:
        validate_name(first_name)
        user['first_name'] = first_name
    if last_name:
        validate_name(last_name)
        user['last_name'] = last_name

    user['updated_at'] = str(datetime.now())

    return jsonify(user)


@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFound('User not found')
    del users[user_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
