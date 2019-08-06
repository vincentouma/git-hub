import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 

    UPLOADED_PHOTOS_DEST ='app/static/photos'


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")




class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:vinceobindi1005@localhost/pitche'
    pass


class ProdConfig(Config):

    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:vinceobindi1005@localhost/pitche'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}