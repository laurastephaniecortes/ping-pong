from flask import render_template
from flask_wtf.csrf import CsrfProtect
from flask_login import current_user
from . import game

from forms import Score

from .. import db
from ..models import Player

@game.route('/game', methods=['GET','POST'])
def home():
    current_user.score += 1

    db.session.commit()
    return render_template('game/score.html')


