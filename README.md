# Intro

This is an AI project @ UI
This gonna be a solution for maze using algorithms:
- BFS
- IDS
- A*

# How to up and run?

first install virtualbox and vagrant on your system.
then follow the steps below.

## create the development server

> host# vagrant up

> host# vagrant ssh

## install dependencies and run project

> box# python -m venv ~/env # creating a virtual env for django

> box# source ~/env/bin/activate # activating the vemv

> box# cd /vagrant/ # going to project path in our vagrant box

> box# pip install -r requirements # installing the requirements

> box# python manage.py runserver 0.0.0.0:8000 # running the server

> box# exit # to exit the box

> host# vagrant halt


## running second time

> host# vagrant up

> host# vagrant ssh

> box# cd /vagrant

> box# pip install -r requirements # installing the requirements

> box# python manage.py runserver 0.0.0.0:8000 # running the server

halt the machine after doing your job.
