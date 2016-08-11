from datetime import datetime
from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class Models(db.Model):

    brand = CharField(unique=True)
    models = TextField(default='')



# create tables
Models.create_table(fail_silently=True)

