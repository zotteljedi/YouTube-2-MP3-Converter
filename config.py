import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'song.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MP3_FOLDER = os.environ.get('MP3_FOLDER') or os.path.join(basedir, 'e:', 'mp3')

