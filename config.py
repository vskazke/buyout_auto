# email server
#  MAIL_SERVER = 'smtp.gmail.com'
MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 465
MAIL_USERNAME = 'anastacia111@yandex.ru'
#  MAIL_USERNAME = 'agafonova.anastasia@gmail.com'
MAIL_PASSWORD = 'rhfcjnrfyfdct100%'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

DATABASE = {
            'name': 'brand.db',
            'engine': 'peewee.SqliteDatabase',
}

DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = 'ssshhhh'

