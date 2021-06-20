class Config(object):
    '''
    Each environment will be a class that inherits from the main class config

    Configurations that will be the same across all environment will go into config,
    while configuration that are specific to an environment will go into the relevant environment below
    '''
    SECRET_KEY = "My$uper$ecretKey4Now"
    SERVER_TIME_ZONE = "Africa/Johannesburg"
    DEFAULT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Production(Config):
    FLASK_ENV = 'production'
    PRODUCTION = True


class Testing(Config):
    FLASK_ENV = 'testing'
    TESTING = True


class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True
