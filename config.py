import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ALCHEMICAL_DATABASE_URL = os.environ.get('ALCHEMICAL_DATABASE_URL')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH') or 4 * 1024 * 1024)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or '25')
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS') or '0')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    APP_NAME = os.environ.get('APP_NAME')
    APP_EMAIL = os.environ.get('APP_EMAIL')
