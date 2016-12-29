from flask import Flask


app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jeevu.g1@gmail.com'
app.config["MAIL_PASSWORD"] = ''

from routes import mail
mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://noobj:noobj@localhost/MailCampaign'

from models import db
db.init_app(app)

import source.routes
