"""Main app/routing file for Twitoff"""

from flask import Flask, render_template
from .models import DB, User,
from .twitter import insert_example_users
from os import getenv

def create_app():
    """Creates and Configures a Flask application"""
    app = Flask(__name__)
    app.config['SQLAlchemy_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False 
    DB.init_app(app)


    @app.route('/')
    def root():
        return render_template("base.html", title="Home", user=User.query.all())

    
    @app.route('/update')
    def update():
        insert_example_users()
        return render_template('base.html',  title="Home", users=User.query.all())
    

    @app.route('/')
    def reset():
        DB.drop_all()
        DB.create_all()
        insert_example_users() 
        return render_template("base.html", title="Home")

    return app 