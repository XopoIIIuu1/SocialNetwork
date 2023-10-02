from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Объявление нашего приложения
app.config.from_object('config')
db = SQLAlchemy(app) # Объявление базы данных

import views
