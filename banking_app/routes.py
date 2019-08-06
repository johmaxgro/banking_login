from flask import render_template, url_for, flash, redirect, request
from banking_app import app, db, bcrypt
from banking_app.models import User
from banking_app.forms import LoginForm, RegisterForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')

@app.route('/main')
def main():
	if not current_user.is_authenticated:
		return redirect(url_for('login'))
	return render_template('main.html', title='Your Online Banking App', header='Your Personal Account')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main'))
	form = RegisterForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
		user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=hash_pw)
		db.session.add(user)
		db.session.commit()
		flash('You are now registered! Log in to reach to Account', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Your Online Banking App', header='Register Your Online Banking Account', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main'))
	form = LoginForm()
	return render_template('login.html', title='Your Online Banking App', header='Log in to your Account', form=form)