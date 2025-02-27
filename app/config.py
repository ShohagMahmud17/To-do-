import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@db/task_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
