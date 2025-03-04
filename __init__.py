from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../instance/config.py')
db = SQLAlchemy(app)

from app import routes, models 