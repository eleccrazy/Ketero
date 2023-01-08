#!/usr/bin/python3
"""
file: search.py
Desc: Responsible for end points related to card orders
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 15 2022
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.hospital import Hospital
from models.user import User
from models.order import Order


@app_views.route("/users/<user_id>/orders", methods=['GET', "POST"])
def orders(user_id=None):
    """Handles http request for orders route without id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if request.method == 'GET':
        # Retrives all order objects linked to the user based on the
        # user id
        objs = storage.all(Order)
        obj_list = [obj.to_dict() for obj in objs.values()
                    if obj.user_id == user_id]
        return jsonify(obj_list), 200

    if request.method == 'POST':
        # Creates a new order object which will be liked the user based
        # on the user id
        data = request.get_json()
        data['user_id'] = user_id
        obj = Order(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201
