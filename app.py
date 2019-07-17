"""
Main application file
"""

from flask import Flask

from models import db
from config import Config
from routes import handler
from predictor import classifier


def create_app(config):
    # Initializes flask object with config
    app = Flask(Config.APP_NAME, template_folder=Config.TEMPLATE_FOLDER)

    # Loads the needed config in the configuration file
    app.config.from_object(Config)

    # Initializes the database and the models, attaching context to app
    db.init_app(app)

    # Handles CORS and other Cross Origin settings 
    # Uses the after request decorator
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', app.config['ALLOWED_ORIGINS'])
        response.headers.add('Access-Control-Allow-Headers', ','.join(app.config['ALLOWED_HEADERS']))
        response.headers.add('Access-Control-Allow-Methods', ','.join(app.config['ALLOWED_METHODS']))
        return response

    app.register_blueprint(handler)
    classifier.load_data(Config.IMAGES_FOLDER)
    classifier.train()

    return app

if __name__ == '__main__':
   app = create_app(None)
   app.run()