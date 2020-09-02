import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db_drop_and_create_all



assistant_token = ''
director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJETkZNVVF4TTBReU9FTXlOVVJDTkVJNU1EQTRRelZGTkRVMU4wRTNOREJETWpJMlJUVTRNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi1tb2hzZW4uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWM4ZTRjNThlMjg2MDAzNzI5MTI4NSIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE1OTkwNzAwMzcsImV4cCI6MTU5OTA3NzIzNywiYXpwIjoiWG45NFdpU2s4ak5OWnlKeFdid3dLT0tXSFB3NGQ1ZnQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwibW9kaWZ5OmFjdG9yIiwibW9kaWZ5Om1vdmllIl19.G0Kqmdj22ivqXCIDjhCzQAv1TqfjkagW89iZu_mcb9niqtahqic4fPr73DjLFfIVFU2hjS2Uc7nyuxF1d3dn-OLy205Lx1SvI9KxGGD9k-pAo17rXrOYTWv5EP1Gx3vpHd48MTUd_Nzxss8e3OvCEr3LyZyHq0yIbQ4698BZf9k1QuwbZNOc0oGTsavN1n4IQfDkkTPelETCFrq2aOy6QYcl0fBmWbwihsyvErzGsSxc05HUyHpR1jb6fsevhiQG0-VSvP4Fx_kWQdiUHgKe7yPf6ymRjtjITDmqK1UVE7cO5Y0GQd4fc0ArDq-0clQJpb2b2-u7YMOUAui94DZZjw'
producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJETkZNVVF4TTBReU9FTXlOVVJDTkVJNU1EQTRRelZGTkRVMU4wRTNOREJETWpJMlJUVTRNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi1tb2hzZW4uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTRiN2UxZjNiMTU1MDAxOTM0NDEyOCIsImF1ZCI6IkNhc3RpbmdBZ2VuY3kiLCJpYXQiOjE1OTkwNjQ1MTksImV4cCI6MTU5OTA3MTcxOSwiYXpwIjoiWG45NFdpU2s4ak5OWnlKeFdid3dLT0tXSFB3NGQ1ZnQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwibW9kaWZ5OmFjdG9yIiwibW9kaWZ5Om1vdmllIl19.eqYQzoIc2dUPaz6hm2-AoxqVjt0ZJjc1O8WDSLehyUahwAIQvHck0VyfmZKG1VG7PT3UGzT9QDawKhihk36eNfVBViVFFcgwzSzUH6Mlj-_7p32nJP0qXeiLO2uGWGWZIlc306cyUY79BifIo_9TyTp3a2HvCTukGsde0fNKQv5r8k9CXkk1qJpDWfe5gEXOZxgGMIN3gmNgZhrCN4O_NLQIDFyTN3yzzt90u2hhcpbn4ZqED_gkbLrQyidUJVVkp7BV3TFRmaeyVH1eq5JmANWAZBac3iCDRqWDT5MZiRL2K-gDgvnyv_MSkMNp3rCzUkF9mlh8kPWnXsf8zUQX1g'


def set_auth_header(role):
    if role == 'assistant':
        return {'Authorization': 'Bearer {}'.format(assistant_token)}
    elif role == 'director':
        return {'Authorization': 'Bearer {}'.format(director_token)}
    elif role == 'producer':
        return {'Authorization': 'Bearer {}'.format(producer_token)}


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Write at least one test for each test for successful operation
    and for expected errors.
    """

### Actors Tests ###

    def test_get_actors(self):
        res = self.client().get('/actors', headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 200)

    def test_get_actors_unauthorized(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)

    def test_add_actor(self):
        new_actor = {
            "name": "New Name",
            "age": 31,
            "gender": "Male"
        }
        res = self.client().post(
            '/actors', json=new_actor, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()['success'], True)

    def test_add_actor_fail(self):
        new_actor = {
        }
        res = self.client().post(
            '/actors', json=new_actor, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 400)

    def test_add_actor_unauthorized(self):
        new_actor = {
            "name": "New Name",
            "age": 31,
            "gender": "Male"
        }
        res = self.client().post(
            '/actors', json=new_actor, headers=set_auth_header(''))
        self.assertEqual(res.status_code, 401)


    def test_modify_actor(self):
        new_actor = {
            "name": "New Name 2",
            "age": 31,
            "gender": "Female"
        }
        res = self.client().patch(
            '/actors/1',
            json=new_actor,
            headers=set_auth_header('director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_modify_actor_unauthorized(self):
        new_actor = {
            "name": "New Name 2",
            "age": 31,
            "gender": "Female"
        }
        res = self.client().patch(
            '/actors/1',
            json=new_actor,
            headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=set_auth_header('director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_nonexistent_actor(self):
        res = self.client().delete('/actors/100000', headers=set_auth_header('director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


### Movies Tests ###

    def test_get_movies(self):
        res = self.client().get('/movies', headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 200)

    def test_get_movies_unauthorized(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 401)

    def test_add_movie(self):
        new_movie = {
            "title": "New Movie",
            "release_date": "Wed, 03 Sep 2020 00:00:00 GMT"
        }
        res = self.client().post(
            '/movies', json=new_movie, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()['success'], True)

    def test_add_movie_fail(self):
        new_movie = {
        }
        res = self.client().post(
            '/movies', json=new_movie, headers=set_auth_header('producer'))
        self.assertEqual(res.status_code, 400)

    def test_add_movie_unauthorized(self):
        new_movie = {
            "title": "New Movie",
            "release_date": "Wed, 04 Sep 2020 00:00:00 GMT"
        }
        res = self.client().post(
            '/movies', json=new_movie, headers=set_auth_header(''))
        self.assertEqual(res.status_code, 401)


    def test_modify_movie(self):
        new_movie = {
            "title": "New Movie 222",
            "release_date": "Wed, 04 Sep 2020 00:00:00 GMT"
        }
        res = self.client().patch(
            '/movies/1',
            json=new_movie,
            headers=set_auth_header('director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_modify_movie_unauthorized(self):
        new_movie = {
            "title": "New Movie 222",
            "release_date": "Wed, 04 Sep 2020 00:00:00 GMT"
        }
        res = self.client().patch(
            '/movies/1',
            json=new_movie,
            headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_nonexistent_movie(self):
        res = self.client().delete('/movies/100000', headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()