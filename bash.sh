#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install Django
pip install Django

# Start a Django project
django-admin startproject config

cd config

# Start a new Django app
python manage.py startapp account