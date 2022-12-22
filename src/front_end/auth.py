#!/usr/bin/python3
"""
file: views.py
Desc: A module responsible for handling all user authentication
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 18 2022
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from uuid import uuid4
from models import storage
from models.user import User
from hashlib import md5
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

cache_id = str(uuid4())


@auth.route('/sign-in', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == "POST":
        data = request.form
        email = data.get('email')
        password = md5(data.get('password').encode()).hexdigest()
        users = storage.all(User).values()
        user = None
        for u in users:
            if u.email == email:
                user = u
                break
        if user:
            if password == user.password:
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password", category='error')
        else:
            flash("Incorrect email address", category='error')
    return render_template("login.html", cache_id=cache_id, user=current_user)


@auth.route('/logout', strict_slashes=False)
def logut():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        users = storage.all(User).values()
        emails = [user.email for user in users]
        phoneNumbers = [user.phone for user in users]
        data = request.form
        email = data.get('email')
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        password1 = data.get('password1')
        password2 = data.get('password2')
        phoneNumber = data.get('phoneNumber')
        if email in emails:
            flash("Email address already exists", category='error')
        elif len(password1) < 6 or len(password1) > 15:
            flash("Password must be 6 - 15 characters length",
                  category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(phoneNumber) != 10:
            flash("Please insert a valid phone number", category='error')
        elif phoneNumber in phoneNumbers:
            flash("Phone number already exists", category='error')
        else:
            info = {"first_name": firstName, "last_name": lastName,
                    "email": email, "phone": phoneNumber, "password": password1}
            new_account = User(**info)
            new_account.save()
            login_user(new_account, remember=True)
            flash("Account created successfully", category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html", cache_id=cache_id, user=current_user)
