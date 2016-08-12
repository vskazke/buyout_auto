from flask import Flask
from flask_peewee.db import Database
#  from flask_debugtoolbar import DebugToolbarExtension
DATABASE = {
        'name': 'brand.db',
        'engine': 'peewee.SqliteDatabase',
}

DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

#  DebugToolbarExtension(app)
db = Database(app)
