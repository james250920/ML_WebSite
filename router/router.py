"""
Router Principal - Rutas API y funcionalidades generales
Contiene todas las rutas que no son vistas específicas (páginas)
Incluye APIs REST, rutas con parámetros, y endpoints de utilidad
"""
import os
from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from services import AudioAnalysisService
from api_config import APIConfig

# Blueprint para rutas API y funcionalidades generales
main_routes = Blueprint('main_routes', __name__)

# Configuración de archivos permitidos
UPLOAD_FOLDER = APIConfig.UPLOAD_FOLDER

# Crear carpeta de uploads si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica si el archivo tiene una extensión permitida"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in APIConfig.ALLOWED_AUDIO_EXTENSIONS


@main_routes.route('/api/analyze', methods=['POST'])
def analyze_audio():
    """
    API para analizar audio - POST
    Recibe un archivo de audio y una acción (detect o identify)
    
    Returns:
        json: Resultado del análisis
    """
    try:
        # Verificar si se envió un archivo
        if 'audio' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No se encontró ningún archivo de audio'
            }), 400
        
        file = request.files['audio']
        action = request.form.get('action', 'detect')
        
        # Verificar que se seleccionó un archivo
        if file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No se seleccionó ningún archivo'
            }), 400
        
        # Verificar extensión del archivo
        if not allowed_file(file.filename):
            return jsonify({
                'status': 'error',
                'message': 'Formato de archivo no permitido. Use: wav, mp3, ogg, flac, m4a, aac'
            }), 400
        
        # Guardar archivo de forma segura
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Analizar calidad del audio
        quality_info = AudioAnalysisService.analyze_audio_quality(filepath)
        
        # Procesar según la acción solicitada
        if action == 'detect':
            # Usar servicio de detección de deepfake
            api_result = AudioAnalysisService.detect_deepfake(filepath)
            
            if 'error' in api_result:
                return jsonify({
                    'status': 'error',
                    'message': api_result['error']
                }), 500
            
            result = {
                'status': 'success',
                'action': 'detect',
                'filename': filename,
                'result': api_result['result'],
                'confidence': api_result['confidence'],
                'details': api_result['details']
            }
            
        elif action == 'identify':
            # Usar servicio de identificación de voz
            api_result = AudioAnalysisService.identify_speaker(filepath)
            
            if 'error' in api_result:
                return jsonify({
                    'status': 'error',
                    'message': api_result['error']
                }), 500
            
            result = {
                'status': 'success',
                'action': 'identify',
                'filename': filename,
                'result': api_result['result'],
                'confidence': api_result['confidence'],
                'details': api_result['details']
            }
        else:
            return jsonify({
                'status': 'error',
                'message': 'Acción no válida'
            }), 400
        
        # Limpiar archivo después del análisis (opcional)
        # os.remove(filepath)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error al procesar el archivo: {str(e)}'
        }), 500


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
