from flask import Flask
from flask_peewee.db import Database
from flask_mail import Mail

#  from flask_debugtoolbar import DebugToolbarExtension
DATABASE = {
        'name': 'brand.db',
        'engine': 'peewee.SqliteDatabase',
}

#  DEBUG = True
#  DEBUG_TB_INTERCEPT_REDIRECTS = False
#  SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
mail = Mail(app)

#  app.config['MAIL_SERVER']='smtp.gmail.com'
#  app.config['MAIL_PORT'] = 465
#  app.config['MAIL_USERNAME'] = 'agafonova.anastasia@gmail.com'
#  app.config['MAIL_PASSWORD'] = 'rhfcjnrfyfdct100%'
#  app.config['MAIL_USE_TLS'] = False
#  app.config['MAIL_USE_SSL'] = True

app.config.from_object('config')


mail = Mail(app)
#  mail.init_app(app)

#  app.config.from_object(__name__)

#  DebugToolbarExtension(app)
db = Database(app)
