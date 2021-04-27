from flask import Flask
from flask_restful import Api, Resource, abort
import sqlite3
import json

app = Flask(__name__)
api = Api(app)


def abort_if_movie_not_found(recomendations):
    if recomendations == None:
        abort(404, message='Movie not found in database.')


class HelloWorld(Resource):
    def get(self, movie_title):
        # ? can this connecting to database be done other way
        conn = sqlite3.connect('movie_recomendations.db')
        cur = conn.cursor()

        cur.execute("SELECT recomendations FROM movie_recomendations WHERE title=?", (movie_title, ))
        recomendations = cur.fetchone()

        abort_if_movie_not_found(recomendations)
        conn.close()

        return {movie_title: recomendations[0]}

api.add_resource(HelloWorld, '/api/<string:movie_title>')

if __name__ == '__main__':
    app.run(debug=True)
