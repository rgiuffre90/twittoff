"""Main app/routing file for Twitoff"""

from flask import Flask, render_template, request
from .models import DB, User
from .twitter import insert_example_users
from os import getenv
from .predict import predict_user

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
    
    @app.route('/compare')
    def compare():
        user0, user1 = sorted([request.values['user1'],
                               request.values['user2']]
                               )
        if user0 == user1:
            message = "Cannot compare users to themselves!"

        else:
            predicition = predict_user(user0, user1, request.values['tweet_text'])
            message = "{} is more likely to be said {} than {}".format(
                request.values['tweet_text'], user1 if predicition else user0,
                user0 if predicition else user1)
        return render_template('predicition.html', title= 'Predicition', message = message)
    
    
    @app.route('/')
    def reset():
        DB.drop_all()
        DB.create_all()
        insert_example_users() 
        return render_template("base.html", title="Home")

    return app 