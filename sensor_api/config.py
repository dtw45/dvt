
# Default config
class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = '\xb7\xb9Q\xac\xa1s\xfe(n}Ez\xdb\xbe\x89o\xf3\xe1\xe0\x7fw\xe8\xeb\xcb'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///senseapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
    TODO: Create a config file that is capable of
    supporting multiple enviornments see below...
    http://flask.pocoo.org/docs/0.12/config/
'''