from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo
)


class RegForm(FlaskForm):
    username = StringField(label="Username", default="Fill this in", validators=[DataRequired(), Length(min=3)])
    password = PasswordField(label="Password", validators=[Length(min=8)])
    confirm  = PasswordField(label="Confirm password", validators=[EqualTo('password', message="Must be same as password.")])
    submit   = SubmitField("Register")

