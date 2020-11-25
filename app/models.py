from flask_login import UserMixin

from app import db, login_manager

class Player(UserMixin, db.Model):

    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    score = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return Player.query.get(int(user_id))

def __repr__(self):
    return self.first_name