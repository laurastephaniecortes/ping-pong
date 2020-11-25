from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired



from ..models import Player

class Score(FlaskForm):
    score = IntegerField('Current Score', validators=[DataRequired()])
    submit = SubmitField('Score')