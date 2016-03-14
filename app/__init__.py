from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.script import Manager
from flask.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

from app import views,models
