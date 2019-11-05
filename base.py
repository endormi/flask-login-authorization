from flask import Blueprint, render_template
from flask_login import login_required, current_user


base = Blueprint('base', __name__)


@base.route('/')
def home():

    return render_template('index.html')


@base.route('/user')
@login_required
def user():
    
    return render_template('user.html', name=current_user.name)
