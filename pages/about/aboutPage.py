"""
About Page - Página de información sobre la aplicación
Contiene el blueprint y las rutas relacionadas con la página about
"""
from flask import Blueprint, render_template

about_page = Blueprint('about_page', __name__)

@about_page.route('/about')
def about():
    """Ruta de la página About"""
    return render_template('about.html')
