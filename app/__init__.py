from flask import Flask

# init the app
app = Flask(__name__, instance_relative_config=True)

# load the view
from app import views

# load the config file
app.config.from_object('config')
