from app import app
from flask import render_template, flash, redirect, url_for, request,session
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')