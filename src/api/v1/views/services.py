#!/usr/bin/python3
"""
file: service.py
Desc: Responsible for end points related to services
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 14 2022
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.service import Service


@app_views.route('/services', methods=['GET', "POST"])
def service_without_id():
    """Handles http request for services route without id"""
    if request.method == 'GET':
        # Retrives all Service objects.
        services = storage.all(Service).values()
        service_list = [s.to_dict() for s in services]
        return jsonify(service_list), 200

    if request.method == 'POST':
        # Creates a new Service object. name is required
        data = request.get_json()
        if data is None:
            abort(400, "Not a Json")
        if data.get("name") is None:
            abort(400, "Missing name")
        obj = Service(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/services/<service_id>', methods=['GET', 'DELETE', 'PUT'])
def service_with_id(service_id=None):
    """Handles http request for services route with id"""
    obj = storage.get(Service, service_id)
    if obj is None:
        abort(404, "Not found")
    if request.method == 'GET':
        # Retrives a Service object based on the service_id.
        return jsonify(obj.to_dict())

    if request.method == 'DELETE':
        # Deletes a Service object based on the service_id.
        obj.delete()
        del obj
        return jsonify({}), 200

    if request.method == 'PUT':
        # Updates a Service object based on the service_id.
        data = request.get_json()
        if data is None:
            abort(400)
        IGNORE = ['id', 'created_at', 'updated_at']
        d = {k: v for k, v in data.items() if k not in IGNORE}
        for k, v in d.items():
            setattr(obj, k, v)
        obj.save()
        return jsonify(obj.to_dict()), 200
