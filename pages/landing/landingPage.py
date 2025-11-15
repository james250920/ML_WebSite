"""
Landing Page - Página principal de la aplicación
Contiene el blueprint y las rutas relacionadas con la página de inicio
"""
from flask import Blueprint, render_template

landing_page = Blueprint('landing_page', __name__)

@landing_page.route('/')
def index():
    """Ruta principal de la aplicación"""
    return render_template('landing.html')

