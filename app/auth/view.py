from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user
from flask_wtf.csrf import CsrfProtect




from . import auth
from forms import Registration, Login 
from .. import db
from ..models import Player


@auth.route('/register', methods=['GET', 'POST'])

def register():
    form = Registration()
    if form.validate_on_submit():
        player = Player(first_name = form.first_name.data)
        db.session.add(player)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
    
    



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        player = Player.query.filter_by(first_name=form.first_name.data).first()
        if player is not None:
            login_user(player)

        return redirect(url_for('game.home'))

    return render_template('auth/login.html', form=form)
    
