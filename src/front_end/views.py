#!/usr/bin/python3
"""
file: views.py
Desc: A module responsible for handling all web-pages
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 18 2022
"""
from flask import Blueprint
from models import storage
from models.service import Service
from models.city import City
from models.hospital import Hospital
from flask import Flask, render_template
from flask_login import login_required, current_user
from uuid import uuid4


views = Blueprint('views', __name__)


@views.route('/home')
@views.route('/')
def home():
    """ Entry point of the web app or home page of the web app"""
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda k: k.name)
    cache_id = str(uuid4())

    services = storage.all(Service).values()
    services = sorted(services, key=lambda k: k.name)

    hospitals = storage.all(Hospital).values()
    hospitals = sorted(hospitals, key=lambda k: k.name)

    return render_template('index.html',
                           cities=cities,
                           services=services,
                           hospitals=hospitals,
                           cache_id=cache_id,
                           user=current_user
                           )


@views.route('/profile')
@login_required
def profile():
    """Profile view of users"""
    return render_template('profile.html', user=current_user)


@views.route('/about')
def about():
    """"About us page"""
    return render_template('about.html', user=current_user)


@views.route('/details')
def details():
    """"Details page for hospitals"""
    return render_template('details.html', user=current_user)
