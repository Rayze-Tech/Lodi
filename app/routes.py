from datetime import datetime
from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import MemberForm
from config import Config

# THIS IS A SECRET DON'T TELL ANYONE
app.secret_key = 'g3@hn!sTC%LtUc@c9Vc%ZBkb^qSD3Hq8w^ZJUZT&j%&n7c5cZD#@R'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/joinus')
def joinus():
    form=MemberForm()
    return render_template('joinus.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')