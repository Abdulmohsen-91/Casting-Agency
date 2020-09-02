import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import json

#database_path = os.environ['DATABASE_URL']
database_name = "casting_agency"
#database_path='postgres://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', database_name)
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    db_init()

'''
db_init()
    initiate the Databse with a dummy data
'''
def db_init():
    new_actor = (Actor(
        name = 'Me',
        gender = 'Male',
        age = 30
        ))

    new_movie = (Movie(
        title = 'My 1st Movie',
        release_date = date.today()
        ))

    new_actor.insert()
    new_movie.insert()
    db.session.commit()

'''
Movie
'''
class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    release_date = Column(Date)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title' : self.title,
            'release_date': self.release_date
        }

    # def __repr__(self):
    #     return json.dumps(self.short())


'''
Actor
'''
class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer)
    gender = Column(String)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name' : self.name,
            'gender': self.gender,
            'age': self.age
        }