#!/usr/bin/python3
"""
file: index.py
Desc: A module which starts the web app
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 18 2022
"""
from front_end import app

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
