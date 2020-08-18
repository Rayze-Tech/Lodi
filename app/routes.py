from datetime import datetime
from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm, ForgetForm
from config import Config
import pyrebase
from firebase import firebase

firebaseConfig={
    "apiKey": "AIzaSyCkPPI25A6y7wdxLJc_JW3zxEWacnWGEQY",
    "authDomain": "autoinsta-64dce.firebaseapp.com",
    "databaseURL": "https://autoinsta-64dce.firebaseio.com",
    "projectId": "autoinsta-64dce",
    "storageBucket": "autoinsta-64dce.appspot.com",
    "messagingSenderId": "516291431121",
    "appId": "1:516291431121:web:70d537636b1f3c48b8d3f0",
    "measurementId": "G-GY6EZVJBH2"
}

direbase = pyrebase.initialize_app(firebaseConfig)
auth = direbase.auth()

from firebase import firebase
firebase = firebase.FirebaseApplication("https://rayze-108b7.firebaseio.com/",None) 

# THIS IS A SECRET DON'T TELL ANYONE
app.secret_key = 'g3@hn!sTC%LtUc@c9Vc%ZBkb^qSD3Hq8w^ZJUZT&j%&n7c5cZD#@R'

@app.route('/')
@app.route('/index')
def index():
    if auth.current_user:
        return render_template('index.html',check=True)
    return render_template('index.html',check=False)

@app.route('/client')
def client(): 
    if auth.current_user:
        userDic=auth.current_user
        token=userDic["localId"]
        try:
            dic = firebase.get('/1W75CnTEOHm89jDZdqh-3lv7H15rZYfQDumN09B9Lzms/users/', token)
            userEmail=dic["userEmail"]
            companyName=dic["companyName"]
            siteDomain=dic["siteDomain"]
            onlinePlat=dic["onlinePlat"]
            softDev=dic["softDev"]
            marketing=dic["marketing"]
            analytics=dic["analytics"]
            SEO=dic["SEO"]
            jobHunt=dic["jobHunt"]
            adsense=dic["adsense"]
            custSup=dic["custSup"]
            googVeri=dic["googVeri"]
            return render_template('client.html',check=True,userEmail=userEmail,companyName=companyName,siteDomain=siteDomain,onlinePlat=onlinePlat,softDev=softDev, marketing=marketing,analytics=analytics,SEO=SEO,jobHunt=jobHunt,adsense=adsense, custSup=custSup,googVeri=googVeri)
        except:
            return render_template('client.html',check=True)
    return render_template('index.html',check=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if auth.current_user:
        return render_template('index.html',check=True)
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    form=LoginForm()
    if request.method == 'POST':
        password = form.password.data
        email = form.email.data
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            userDic=auth.current_user
            token=userDic["localId"]
            try:
                dic = firebase.get('/1W75CnTEOHm89jDZdqh-3lv7H15rZYfQDumN09B9Lzms/users/', token)
                userEmail=dic["userEmail"]
                companyName=dic["companyName"]
                siteDomain=dic["siteDomain"]
                onlinePlat=dic["onlinePlat"]
                softDev=dic["softDev"]
                marketing=dic["marketing"]
                analytics=dic["analytics"]
                SEO=dic["SEO"]
                jobHunt=dic["jobHunt"]
                adsense=dic["adsense"]
                custSup=dic["custSup"]
                googVeri=dic["googVeri"]
                return render_template('client.html',check=True,userEmail=userEmail,companyName=companyName,siteDomain=siteDomain,onlinePlat=onlinePlat,softDev=softDev, marketing=marketing,analytics=analytics,SEO=SEO,jobHunt=jobHunt,adsense=adsense, custSup=custSup,googVeri=googVeri)
            except:
                return render_template('client.html',check=True)
        except KeyError:
            return render_template('login.html', us=unsuccessful,form=form)
        except:
            return render_template('login.html', us=unsuccessful,form=form)
    return render_template('login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if auth.current_user:
        return render_template('index.html',check=True)
    unsuccessful = 'Account may already exist or password may not be secure enough'
    successful = 'Account Creation successful'
    form=RegistrationForm()
    if request.method == 'POST':
        password = form.password.data
        email = form.email.data
        try:
            user = auth.create_user_with_email_and_password(email, password)
            #START
            unsuccessful = 'Please check your credentials'
            successful = 'Login successful'
            form=LoginForm()
            if request.method == 'POST':
                password = form.password.data
                email = form.email.data
                try:
                    user = auth.sign_in_with_email_and_password(email, password)
                    userDic=auth.current_user
                    token=userDic["localId"]
                    try:
                        dic = firebase.get('/1W75CnTEOHm89jDZdqh-3lv7H15rZYfQDumN09B9Lzms/users/', token)
                        userEmail=dic["userEmail"]
                        companyName=dic["companyName"]
                        siteDomain=dic["siteDomain"]
                        onlinePlat=dic["onlinePlat"]
                        softDev=dic["softDev"]
                        marketing=dic["marketing"]
                        analytics=dic["analytics"]
                        SEO=dic["SEO"]
                        jobHunt=dic["jobHunt"]
                        adsense=dic["adsense"]
                        custSup=dic["custSup"]
                        googVeri=dic["googVeri"]
                        return render_template('client.html',check=True,userEmail=userEmail,companyName=companyName,siteDomain=siteDomain,onlinePlat=onlinePlat,softDev=softDev, marketing=marketing,analytics=analytics,SEO=SEO,jobHunt=jobHunt,adsense=adsense, custSup=custSup,googVeri=googVeri)
                    except:
                        return render_template('client.html',check=True)
                except KeyError:
                    return render_template('login.html', us=unsuccessful,form=form)
                except:
                    return render_template('login.html', us=unsuccessful,form=form)
            return render_template('login.html',form=form)
            #END
        except KeyError:
            return render_template('register.html', us=unsuccessful,form=form)
        except:
            return render_template('register.html', us=unsuccessful,form=form)
    return render_template('register.html',form=form)

@app.route('/logout')
def logout():
    auth.current_user = None
    return render_template('index.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if auth.current_user:
        return render_template('index.html',check=True)
    unsuccessful = 'Email is not associated with an account'
    successful = 'Recovery email sent'
    form=ForgetForm()
    if request.method == 'POST':
        email = form.email.data
        try:
            auth.send_password_reset_email(email)
            return render_template('reset.html', s=successful,form=form)
        except KeyError:
            return render_template('reset.html', us=unsuccessful,form=form)
        except:
            return render_template('reset.html', us=unsuccessful,form=form)
    return render_template('reset.html',form=form)