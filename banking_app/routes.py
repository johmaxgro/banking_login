from flask import render_template
from banking_app import app


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Welcome to your Banking App!') 

@app.route('/main')
def main():
    return '<h1>You are logged in!</h1>'