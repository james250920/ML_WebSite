import os

class APIConfig:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac', 'm4a', 'aac'}
    ML_BACKEND_URL = os.environ.get('ML_BACKEND_URL', 'http://localhost:8000')
    ML_PREDICT_ENDPOINT = '/api/dl/predict'
    DEEPFAKE_API_URL = os.environ.get('DEEPFAKE_API_URL', 'http://localhost:8000/api/dl/predict')
    DEEPFAKE_API_KEY = os.environ.get('DEEPFAKE_API_KEY', '')
    VOICE_ID_API_URL = os.environ.get('VOICE_ID_API_URL', 'http://localhost:8000/api/ml/predict')
    VOICE_ID_API_KEY = os.environ.get('VOICE_ID_API_KEY', '')
    RESPONSE_TIMEOUT = 30
