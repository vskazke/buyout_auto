# email server
#  MAIL_SERVER='smtp.gmail.com'
MAIL_SERVER='smtp.yandex.ru'
MAIL_PORT = 465
#  MAIL_PORT = 587
#  MAIL_USE_TLS = True
#  MAIL_USE_SSL = False
#  MAIL_PORT = 465
#  MAIL_USERNAME = 'agafonova.anastasia@gmail.com'
MAIL_USERNAME = 'anastacia111@yandex.ru'
MAIL_PASSWORD = 'rhfcjnrfyfdct100%'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

DATABASE = {
            'name': 'brand.db',
            'engine': 'peewee.SqliteDatabase',
}
DATABASE_URL = 'postgres://tvytmuwokzsmya:1TUGncKOoEGvv84xleyzA-Q7Wu@ec2-50-19-223-15.compute-1.amazonaws.com:5432/dbnr8s4sdrj19n'


DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = 'ssshhhh'

