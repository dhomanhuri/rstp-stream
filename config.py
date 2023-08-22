import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    UPLOAD_FOLDER = str(os.environ.get('UPLOAD_FOLDER'))
    MAX_CONTENT_LENGTH = 2*1024*1024