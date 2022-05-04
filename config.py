import os

class Config:
    """Parent Config Class """
    BASE_URL = 'https://newsapi.org/v2/top-headlines?q=news&apiKey={}'
    SOURCES_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    LOCAL_URL = 'https://newsapi.org/v2/everything?q=kenya&apiKey={}'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    API_KEY = os.environ.get("API_KEY")

class ProdConfig(Config):
    """Production Config Class"""


class DevConfig(Config):
    """Developement Config"""
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}