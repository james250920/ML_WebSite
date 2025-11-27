"""
Configuración de APIs externas y servicios
"""
import os

class APIConfig:
    """Configuración de APIs"""
    
    # Carpetas de archivos
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB máximo
    
    # Extensiones de archivo permitidas
    ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac', 'm4a', 'aac'}
    
    # API Backend de ML
    ML_BACKEND_URL = os.environ.get('ML_BACKEND_URL', 'http://localhost:8000')
    ML_PREDICT_ENDPOINT = '/api/ml/predict'
    
    # APIs externas (ejemplos - reemplazar con tus APIs reales)
    # API para detección de deepfake
    DEEPFAKE_API_URL = os.environ.get('DEEPFAKE_API_URL', 'http://localhost:8000/api/ml/predict')
    DEEPFAKE_API_KEY = os.environ.get('DEEPFAKE_API_KEY', '')
    
    # API para identificación de voz
    VOICE_ID_API_URL = os.environ.get('VOICE_ID_API_URL', 'http://localhost:8000/api/ml/predict')
    VOICE_ID_API_KEY = os.environ.get('VOICE_ID_API_KEY', '')
    
    # Configuración de respuestas
    RESPONSE_TIMEOUT = 30  # segundos
