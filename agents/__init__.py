from flask import Flask
from routes import main  # adjust if needed based on your folder structure

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
