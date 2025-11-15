"""
Aplicación principal Flask - ML Website
Punto de entrada de la aplicación
"""
import os
from flask import Flask
from config import config
from pages.landing.landingPage import landing_page
from pages.about.aboutPage import about_page
from router.router import main_routes

def create_app(config_name='default'):
    """
    Factory pattern para crear la aplicación Flask
    
    Args:
        config_name (str): Nombre de la configuración a usar
        
    Returns:
        Flask: Instancia de la aplicación configurada
    """
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Registrar blueprints
    app.register_blueprint(landing_page)
    app.register_blueprint(about_page)
    app.register_blueprint(main_routes)
    
    return app

if __name__ == '__main__':
    # Obtener el entorno de la variable de entorno o usar 'development' por defecto
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(env)
    
    # Ejecutar la aplicación
    app.run(
        debug=app.config['DEBUG'],
        host='0.0.0.0',
        port=5000
    )