"""Main app/routing file for Twitoff"""

from flask import Flask, render_template
from .models import DB, User, Tweet, insert_example_users

def create_app():
    """Creates and Configures a Flask application"""
    app = Flask(__name__)
    app.config['SQLAlchemy_DATABASE_URI'] = "sqlite://db/sqlite3"
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False 
    DB.init_app(app)


    @app.route('/')
    def root():
        DB.drop_all() # deletes already present databases
        DB.create_all() # creates the database from scratch
        insert_example_users() 
        return render_template("base.html", title="Home", users=User.query.all())

    return app 