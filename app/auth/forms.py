from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired



from ..models import Player


class Registration(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_name(self, field):
        if Player.query.filter_by(first_name = field.data).first():
            raise ValidationError('name is already registered')
    


class Login(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Login')