from flask import render_template, url_for, flash, redirect, request
from banking_app import app, db, bcrypt
from banking_app.models import User
from banking_app.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')

@app.route('/main')
def main():
	if not current_user.is_authenticated:
		return redirect(url_for('login'))
	return render_template('main.html', title='Your Online Banking App', header='Your Personal Account')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main'))
	form = LoginForm()
	return render_template('login.html', title='Your Online Banking App', header='Log in to your Account', form=form)