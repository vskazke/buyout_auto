from flask import Flask
#  from flask_debugtoolbar import DebugToolbarExtension

DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

#  DebugToolbarExtension(app)
