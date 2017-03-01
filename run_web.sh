#!/bin/bash

# Update Database Schema
echo '----LOADING DATABASE SCHEMA---'
python ./manage.py migrate --noinput

# Create default superuser
echo '----LOADING DEFAULT SUPER USER---'
python ./manage.py createdefaultuser

# Create dummy data
echo '----LOADING DUMMY DATA----'
python ./manage.py loaddummydata

# Start development server
echo '----STARTING DEVELOPMENT SERVER at http://127.0.0.1:8000----'
python ./manage.py runserver 0.0.0.0:8000