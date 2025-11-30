import requests
import os
from api_config import APIConfig

class AudioAnalysisService:
    
    @staticmethod
    def detect_deepfake(audio_path):
        try:
            with open(audio_path, 'rb') as audio_file:
                files = {'file': (os.path.basename(audio_path), audio_file, 'audio/wav')}
                url = APIConfig.ML_BACKEND_URL + APIConfig.ML_PREDICT_ENDPOINT
                
                response = requests.post(
                    url,
                    files=files,
                    timeout=APIConfig.RESPONSE_TIMEOUT
                )
                
                if response.status_code == 200:
                    api_data = response.json()
                    prediction_data = api_data.get('prediction', {})
                    label = prediction_data.get('label', 'DESCONOCIDO')
                    confidence = prediction_data.get('confidence', 0)
                    is_deepfake = prediction_data.get('is_deepfake', False)
                    probabilities = api_data.get('probabilities', {})
                    
                    return {
                        'status': 'success',
                        'result': label,
                        'confidence': confidence,
                        'details': {
                            'authenticity': label,
                            'is_deepfake': is_deepfake,
                            'probability': confidence / 100,
                            'analysis': f'Audio clasificado como {label} con {confidence}% de confianza',
                            'probabilities': probabilities,
                            'technical_details': api_data.get('audio_info', {})
                        }
                    }
                else:
                    return {
                        'error': f'Error en la API: {response.status_code}',
                        'status': 'error',
                        'message': response.text
                    }
            
        except requests.exceptions.Timeout:
            return {
                'error': 'Timeout al conectar con la API',
                'status': 'error',
                'message': 'El servidor tardó demasiado en responder'
            }
        except requests.exceptions.ConnectionError:
            return {
                'error': 'No se pudo conectar con el servidor backend',
                'status': 'error',
                'message': 'Verifica que el backend esté ejecutándose en http://localhost:8000'
            }
        except Exception as e:
            return {
                'error': f'Error inesperado: {str(e)}',
                'status': 'error',
                'message': str(e)
            }
    
    @staticmethod
    def identify_speaker(audio_path):
        try:
            with open(audio_path, 'rb') as audio_file:
                files = {'file': (os.path.basename(audio_path), audio_file, 'audio/wav')}
                url = APIConfig.ML_BACKEND_URL + APIConfig.ML_PREDICT_ENDPOINT
                
                response = requests.post(
                    url,
                    files=files,
                    timeout=APIConfig.RESPONSE_TIMEOUT
                )
                
                if response.status_code == 200:
                    api_data = response.json()
                    prediction_data = api_data.get('prediction', {})
                    label = prediction_data.get('label', 'DESCONOCIDO')
                    confidence = prediction_data.get('confidence', 0)
                    
                    return {
                        'status': 'success',
                        'result': 'Función en desarrollo',
                        'confidence': confidence,
                        'details': {
                            'identified': False,
                            'speaker': 'No disponible',
                            'probability': confidence / 100,
                            'message': 'La identificación de hablante estará disponible próximamente',
                            'current_analysis': f'Audio detectado como {label}'
                        }
                    }
                else:
                    return {
                        'error': f'Error en la API: {response.status_code}',
                        'status': 'error',
                        'message': response.text
                    }
            
        except requests.exceptions.Timeout:
            return {
                'error': 'Timeout al conectar con la API',
                'status': 'error'
            }
        except requests.exceptions.ConnectionError:
            return {
                'error': 'No se pudo conectar con el servidor backend. Verifica que esté ejecutándose en http://localhost:8000',
                'status': 'error'
            }
        except Exception as e:
            return {
                'error': f'Error inesperado: {str(e)}',
                'status': 'error'
            }
    
    @staticmethod
    def analyze_audio_quality(audio_path):
        file_size = os.path.getsize(audio_path)
        file_extension = os.path.splitext(audio_path)[1].lower()
        return {
            'file_size': file_size,
            'format': file_extension,
            'quality': 'Acceptable' if file_size > 10000 else 'Low'
        }
