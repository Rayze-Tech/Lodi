import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'g3@hn!sTC%LtUc@c9Vc%ZBkb^qSD3Hq8w^ZJUZT&j%&n7c5cZD#@R'