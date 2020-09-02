# Casting Agency Capstone

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

First ensure you are working from your created virtual environment.


To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` to point to the application. 

To execute tests, run:
```bash 
python test_app.py
```

## API Documentation

Below are all endpoints and what methods are used.

### Application accessibility

All APIs can only be accessed via this link 
**_https://casting-agency-mohsen.herokuapp.com/_**

##### 1. GET '/actors'
##### 2. GET '/movies'
##### 3. POST '/actors'
##### 4. POST '/movies'
##### 5. PATCH '/actors/<int:id>'
##### 6. PATCH '/movies/<int:id>'
##### 7. DELETE '/actors/<int:id>'
##### 8. DELETE '/movies/<int:id>'