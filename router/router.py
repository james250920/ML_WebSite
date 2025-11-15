"""
Router Principal - Rutas API y funcionalidades generales
Contiene todas las rutas que no son vistas específicas (páginas)
Incluye APIs REST, rutas con parámetros, y endpoints de utilidad
"""
from flask import Blueprint, jsonify, request

# Blueprint para rutas API y funcionalidades generales
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/user/<nombre>')
def user(nombre):
    """
    Ruta de ejemplo con parámetros dinámicos
    
    Args:
        nombre (str): Nombre del usuario a saludar
        
    Returns:
        str: HTML con saludo personalizado
    """
    return f'<h2>Hola, {nombre}!</h2>'


@main_routes.route('/api/hello')
def api_hello():
    """
    API de ejemplo - GET
    Devuelve un mensaje JSON simple
    
    Returns:
        json: Mensaje de saludo en formato JSON
    """
    return jsonify({
        'mensaje': 'Hola desde la API',
        'status': 'success'
    })


@main_routes.route('/api/datos', methods=['POST'])
def recibir_datos():
    """
    API para recibir datos - POST
    Recibe datos JSON y los devuelve confirmando la recepción
    
    Returns:
        json: Datos recibidos y mensaje de confirmación
    """
    datos = request.get_json()
    return jsonify({
        'recibido': datos,
        'mensaje': 'Datos procesados correctamente'
    })
