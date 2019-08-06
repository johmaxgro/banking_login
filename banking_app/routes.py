from flask import render_template, url_for, flash, redirect, request
from banking_app import app, db, bcrypt
from banking_app.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Welcome to your Banking App!') 

@app.route('/main')
def main():
    return '<h1>You are logged in!</h1>'