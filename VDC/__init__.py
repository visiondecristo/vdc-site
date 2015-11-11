from flask import Flask

app = Flask(__name__)



WTF_CSRF_ENABLED = True
app.secret_key = ''

#Administrator
ADMIN = 'cjusto777@gmail.com'

TITLE = 'Vision De Cristo'
#SMTP Settings

app.config.update(dict(
MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 465,
MAIL_USE_SSL = True,
MAIL_USERNAME = 'cjusto777@gmail.com',
MAIL_PASSWORD = '',

))

from routes import mail
mail.init_app(app)

import VDC.routes