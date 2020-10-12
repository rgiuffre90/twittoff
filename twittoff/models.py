"""SQLAlchemy models and utility functions for TwitOff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter Users corresponding to Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Tweet(DB.Model):
    """Tweet related to a user"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.String)
    
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_users():
    """ Example users """
    bill = User(id=1, name="BillGates")
    elon = User(id=2, name="ElonMusk")
    DB.session.add(bill)
    DB.session.add(elon)

    """ Example Tweets """
    bt1 = Tweet(id=1, text="Microsoft is great", user=bill)
    bt2 = Tweet(id=2, text="Buy Xbox", user=bill)
    bt3 = Tweet(id=3, text="Windows is not buggy", user=bill)
    et1 = Tweet(id=4, text="Go to Mars", user=elon)
    et2 = Tweet(id=5, text="Buy a Tesla",  user=elon)
    et3 = Tweet(id=6, text="Boring Company", user=elon)
    DB.session.add(bt1)
    DB.session.add(bt2)
    DB.session.add(bt3)
    DB.session.add(et1)
    DB.session.add(et2)
    DB.session.add(et3)
    DB.session.commit()