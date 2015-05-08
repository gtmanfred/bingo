import os
class Config(object):
    CSRF_ENABLED = True
    DEVEL = False
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/bingo')
    STORMPATH_API_KEY_FILE = os.path.expanduser('~/.apiKey.properties')
    STORMPATH_APPLICATION = 'bingo'
    STORMPATH_ENABLE_USERNAME = True
    STORMPATH_ENABLE_GIVEN_NAME = False
    STORMPATH_ENABLE_SURNAME = False
    STORMPATH_ENABLE_MIDDLE_NAME = False
    STORMPATH_REQUIRE_USERNAME = True
    STORMPATH_REQUIRE_GIVEN_NAME = False
    STORMPATH_REQUIRE_MIDDLE_NAME = False
    STORMPATH_REQUIRE_SURNAME = False

    STORMPATH_ENABLE_FORGOT_PASSWORD = True

class TestingConfig(Config):
    DEVEL = True
