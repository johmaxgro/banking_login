from flask import Flask
from banking_app import app


@app.route('/')
@app.route('/login')
def login():
    return '<h1>Your Online Banking App!</h1>'

@app.route('/main')
def main():
    return '<h1>You are logged in!</h1>'