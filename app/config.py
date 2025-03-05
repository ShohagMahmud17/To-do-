import os

class Config:
    SECRET_KEY = 'supersecretkey'
    MYSQL_DATABASE = 'mysql://root:root@db/task_manager'
    MYSQL_TRACK_MODIFICATIONS = False
