import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor, db_drop_and_create_all

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  #CORS(app)

  setup_db(app)
  '''
  !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
  !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
  '''
  db_drop_and_create_all()

  @app.route('/')
  def index():
    return "Welcome!!! We Are A Casting Agency!!!"
  

  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(token):
    try:
      actors = Actor.query.all()
      all_actors = [actor.format() for actor in actors]
      print(all_actors)
      return jsonify({
        'success': True,
        'actors': all_actors
        })
    except:
      abort(401)


  @app.route('/actors', methods=['POST'])
  @requires_auth('add:actor')
  def add_actor(token):
    try:
      body = request.get_json()


      name = body.get('name')
      age = body.get('age')
      gender = body.get('gender')

      if body is None:
        abort(422)

      if not name or not age or not gender:
        abort(422)
      

      actor = Actor(name=name, age=age, gender=gender)
      actor.insert()

      return jsonify({
        'success': True,
        'created': actor.id
      }), 201
    except:
        abort(400)


  @app.route('/actors/<int:id>', methods=["PATCH"])
  @requires_auth('modify:actor')
  def modify_actor(jwt, id):
    try:
      actor = Actor.query.get(id)

      body = request.get_json()
      name = body.get('name')
      age = body.get('age')
      gender = body.get('gender')

      if body is None:
        abort(422)

      actor.name = name
      actor.age = age
      actor.gender = gender

      actor.update()

      return jsonify({
        'success': True,
        'modified': id
      })
    except:
        abort(400)


  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor(jwt, id):
    actor_id = Actor.query.get(id)

    if not actor_id:
      abort(404)

    try:
      actor_id.delete()

      return jsonify({
          'success': True, 'delete': id
      })
    except:
      abort(422)


  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(token):
    try:
      movies = Movie.query.all()
      all_movies = [movie.format() for movie in movies]
      print(all_movies)
      return jsonify({
        'success': True,
        'movies': all_movies
        })
    except:
      abort(401)


  @app.route('/movies', methods=['POST'])
  @requires_auth('add:movie')
  def add_movie(token):
    try:
      body = request.get_json()

      title = body.get('title')
      release_date = body.get('release_date')

      if body is None:
        abort(422)

      if not title or not release_date:
        abort(422)

      movie = Movie(title=title, release_date=release_date)
      movie.insert()

      return jsonify({
          'success': True,
          'created': movie.id
      }), 201
    except:
        abort(400)


  @app.route('/movies/<int:id>', methods=["PATCH"])
  @requires_auth('modify:movie')
  def modify_movie(jwt, id):
    try:
      movie = Movie.query.get(id)

      body = request.get_json()
      title = body.get('title')
      release_date = body.get('release_date')

      if body is None:
        abort(422)

      movie.title = title
      movie.release_date = release_date

      movie.update()

      return jsonify({
        'success': True,
        'modified': id
      })
    except:
        abort(400)

  
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(jwt, id):
    movie_id = Movie.query.get(id)

    if not movie_id:
      abort(404)

    try:
      movie_id.delete()

      return jsonify({
        'success': True, 'delete': id
      })
    except:
      abort(422)




  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code


  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)