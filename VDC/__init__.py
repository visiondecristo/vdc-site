from flask import Flask

app = Flask(__name__)



WTF_CSRF_ENABLED = True
app.secret_key = 'x1c\x07O\xa3\xce\x80\x9eQ\x8f\xd19\xd3\xe8\xd3n|k\xe1\xc2\x10\xef\xe6\xc8,'

#Administrator
ADMIN = 'cjusto777@gmail.com'

TITLE = 'Vision De Cristo'
#SMTP Settings

app.config.update(dict(
MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 465,
MAIL_USE_SSL = True,
MAIL_USERNAME = 'cjusto777@gmail.com',
MAIL_PASSWORD = 'Saved777',

))

from routes import mail
mail.init_app(app)

import VDC.routes