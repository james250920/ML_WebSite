import os
from flask import Flask
from config import config
from pages.landing.landingPage import landing_page
from pages.about.aboutPage import about_page
from router.router import main_routes

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(landing_page)
    app.register_blueprint(about_page)
    app.register_blueprint(main_routes)
    return app

if __name__ == '__main__':
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(env)
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)