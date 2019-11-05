from flask import Blueprint, redirect, url_for, render_template


authenticate = Blueprint('__auth__', __name__)


@authenticate.route('/signin')
def signin():
    return render_template('sign_in.html')


@authenticate.route('/signup')
def signup():
    return render_template('sign_up.html')


@authenticate.route('/logout')
def logout():
    return redirect(url_for('base.home'))
