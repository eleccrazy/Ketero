#!/usr/bin/python3
"""
file: hospital.py
Desc: Responsible for end points related to hospitals
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 14 2022
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.hospital import Hospital
from models.city import City


@app_views.route('/cities/<city_id>/hospitals', methods=['GET', "POST"])
def hospital_without_id(city_id=None):
    """Handles http request for hospitals route without id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if request.method == 'GET':
        # Retrives all Hospital objects linked to a City object based
        # on the city_id
        objs = storage.all(Hospital)
        obj_list = [obj.to_dict() for obj in objs.values()
                    if obj.city_id == city_id]
        return jsonify(obj_list), 200

    if request.method == 'POST':
        # Creates a new Hospital object, which will be linked to a City
        # object based on the city_id
        data = request.get_json()
        if data is None:
            abort(400, "Not a Json")
        if data.get("name") is None:
            abort(400, "Missing name")
        if data.get("image_url") is None:
            abort(400, "Missing image_url")
        data['city_id'] = city_id
        obj = Hospital(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/hospitals/<hospital_id>', methods=['GET', 'DELETE', 'PUT'])
def hospital_with_id(hospital_id=None):
    """Handles http request for hospitals route with id"""
    obj = storage.get(Hospital, hospital_id)
    if obj is None:
        abort(404, "Not found")
    if request.method == 'GET':
        # Retrives a Hospital object based on the hospital_id.
        return jsonify(obj.to_dict())

    if request.method == 'DELETE':
        # Deletes a Hospital object based on the hospital_id.
        obj.delete()
        del obj
        return jsonify({}), 200

    if request.method == 'PUT':
        # Updates a Hospital object based on the hospital_id.
        data = request.get_json()
        if data is None:
            abort(400)
        IGNORE = ['id', 'created_at', 'updated_at', 'city_id']
        d = {k: v for k, v in data.items() if k not in IGNORE}
        for k, v in d.items():
            setattr(obj, k, v)
        obj.save()
        return jsonify(obj.to_dict()), 200
