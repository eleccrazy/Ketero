#!/usr/bin/python3
"""
file: cities.py
Desc: Responsible for end points related to cities
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 14 2022
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.city import City


@app_views.route('/cities', methods=['GET', "POST"])
def city_without_id():
    """Handles http request for cities route without id"""
    if request.method == 'GET':
        # Retrives all City objects.
        cities = storage.all(City).values()
        cities_list = [c.to_dict() for c in cities]
        return jsonify(cities_list), 200

    if request.method == 'POST':
        # Creates a new city object. Name is a required filled.
        data = request.get_json()
        if data is None:
            abort(400, "Not a Json")
        if data.get("name") is None:
            abort(400, "Missing name")
        obj = City(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def city_with_id(city_id=None):
    """Handles http request for cities route with id"""
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404, "Not found")
    if request.method == 'GET':
        # Retrives a City object based on the city_id.
        return jsonify(obj.to_dict())

    if request.method == 'DELETE':
        # Deletes a City object based on the city_id.
        obj.delete()
        del obj
        return jsonify({}), 200

    if request.method == 'PUT':
        # Updates a City object based on the city_id.
        data = request.get_json()
        if data is None:
            abort(400)
        IGNORE = ['id', 'created_at', 'updated_at']
        d = {k: v for k, v in data.items() if k not in IGNORE}
        for k, v in d.items():
            setattr(obj, k, v)
        obj.save()
        return jsonify(obj.to_dict()), 200
