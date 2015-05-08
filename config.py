import os
class Config(object):
    CSRF_ENABLED = True
    DEVEL = False
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/bingo')

class TestingConfig(Config):
    DEVEL = True
