# CLIENTS REST API




## _Access to the functions for handling for management clients.

This API  uses some open-source projects to work properly:

- [Django Rest Framework] - evented I/O for the backend
- [SqlLite] - relational database management system

## Purpose
The purpose of this repository is to demonstrate some techniques for building a REST API using the Django Rest Framework.

## Installation

Requires [Django](https://nodejs.org/) v2.2.24+ to run.

Install the dependencies and devDependencies and start the server.

### Development
```sh
cd api
create the virtual environment: python -m venv nameEnvironment
activate the virtual environment: .\nameEnvironment\Scripts\Activate.bat
install dependencies: pip install -r requirements.txt
Starting development server at http://127.0.0.1:8000/
Create a database named api en sqlLite;
send migrations: python manage.py migrate
create super user: python manage.py createsuperuser
make migrations: python manage.py makemigrations 
send migrations: python manage.py migrate
run the server: python manage.py runserver

Starting development server at http://127.0.0.1:8000/ and view endpoint
enter the api documentation path: http://127.0.0.1:8000/swagger/

```

## Plugins

| Plugin | README |
| ------ | ------ |
| Json Web Token | [plugins/jsonwebtoken/README.md][PlJw] |



