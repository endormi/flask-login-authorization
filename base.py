from flask import Blueprint, render_template


base = Blueprint('base', __name__)


@base.route('/')
def home():
    return render_template('index.html')


@base.route('/user')
def user():
    return render_template('user.html')
