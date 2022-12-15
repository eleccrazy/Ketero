#!/usr/bin/python3
"""
file: search.py
Desc: Responsible for end points related to searching hospitals
      Depending on different payloads.
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 15 2022
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.service import Service
from models.city import City
from models.hospital import Hospital


@app_views.route("/hospital_search", methods=["POST"])
def hospital_search():
    """Handles HTTP POST request for hospital search route"""
    if request.method == "POST":
        # Retrives all Hospital objects depending of the JSON in the
        # body of the request.
        data = request.get_json()
        if data is None:
            abort(400, "Not a Json")
        if data and len(data):
            cities = data.get('cities', None)
            services = data.get('services', None)
        if not data or not len(data) or (
                not cities and
                not services):
            hospitals = storage.all(Hospital).values()
            list_hospitals = []
            [list_hospitals.append(h.to_dict()) for h in hospitals]
            return jsonify(list_hospitals)
        list_hospitals = []
        if cities:
            city_obj = [storage.get(City, c_id) for c_id in cities]
            for city in city_obj:
                if city:
                    for hospital in city.hospitals:
                        if hospital not in list_hospitals:
                            list_hospitals.append(hospital)
        if services:
            if not list_hospitals:
                list_hospitals = storage.all(Hospital).values()
            services_obj = [storage.get(Service, s_id) for s_id in services]
            list_hospitals = [hospital for hospital in list_hospitals
                              if all([s in hospital.services
                                      for s in services_obj])]
        hospitals = []
        for hospital in list_hospitals:
            d = hospital.to_dict()
            d.pop('services', None)
            hospitals.append(d)

        return jsonify(hospitals)
