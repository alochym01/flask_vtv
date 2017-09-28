from flask import Blueprint, render_template

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import Email, InputRequired, Length

users = Blueprint('users', __name__, template_folder='templates')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('remember me')


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>%s\t%s\t</h1>' % (form.username.data, form.password.data)
    return render_template('users/login.html', form=form)
