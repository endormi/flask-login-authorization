from flask import Blueprint, redirect, url_for, render_template, flash, request
from .users import __user__
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from . import db


authenticate = Blueprint('__auth__', __name__)


@authenticate.route('/signin', methods=['POST'])
def __signin__():
    email = request.form.get('email')
    password = request.form.get('password')
    checked = True if request.form.get('remember') else False

    _user_ = __user__.query.filter_by(email=email).first()

    if not _user_ or not check_password_hash(_user_.password, password):
        flash('Email address or password is not correct.')
        return redirect(url_for('__auth__.signin'))

    login_user(_user_, remember=checked)

    return redirect(url_for('base.user'))


@authenticate.route('/signin')
def signin():

    return render_template('sign_in.html')


@authenticate.route('/signup', methods=['POST'])
def __signup__():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    _user_ = __user__.query.filter_by(email=email).first()

    if _user_:
        flash('Email address already exists.')
        return redirect(url_for('__auth__.signup'))

    __new__ = __user__(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha512'))

    db.session.add(__new__)
    db.session.commit()

    return redirect(url_for('__auth__.signin'))


@authenticate.route('/signup')
def signup():

    return render_template('sign_up.html')


@authenticate.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('base.home'))
