from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kbxvjubqsnanxs:b617701e452cebd4a124af3d15825d7d22ae7be3b6c935a884ced2100c27346f@ec2-50-17-227-28.compute-1.amazonaws.com:5432/d4vkmlg5edqhnc"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Config Values
# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'
# needed for session security, the flash() method in this case stores the message
# in a session
SECRET_KEY = 'Sup3r$3cretkey'


app.config.from_object(__name__)

from app import views