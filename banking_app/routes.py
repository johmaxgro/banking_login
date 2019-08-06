from flask import render_template, url_for, flash, redirect, request, session
from banking_app import app, db, bcrypt
from banking_app.models import User
from banking_app.forms import LoginForm, RegisterForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')

@app.route('/main')
def main():
	if not current_user.is_authenticated:
		return redirect(url_for('login'))
	# user = session['current_user']
	return render_template('main.html', title='Your Online Banking App', header='Your Personal Account', user=current_user)

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
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=True)
			# session['current_user'] = user
			return redirect(url_for('main', user=user))
		else:
			flash('Login failed. Please check if your email and password are correct.', 'danger')
	return render_template('login.html', title='Your Online Banking App', header='Log in to your Account', form=form)

