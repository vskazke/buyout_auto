from datetime import datetime
from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class Brands(db.Model):

    brand = CharField(unique=True)
    icon = CharField(default='')
    #  def __unicode__(self):
        #  return self.brand


class Models(db.Model):

    brand = ForeignKeyField(Brands)
    models = TextField(default='')
    join_date   = CharField(default=datetime.now)

    #  def __unicode__(self):
        #  return 'id: %s, donor: %s' % (
            #  self.id, self.donor.brand)

class Years(db.Model):

    year = CharField(unique=True)



# create tables
Brands.create_table(fail_silently=True)
Models.create_table(fail_silently=True)
Years.create_table(fail_silently=True)

