
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import main  # Absolute import
    app.register_blueprint(main)

    return app
