"""
Servicios para consumir APIs externas
"""
import requests
import os
from api_config import APIConfig

class AudioAnalysisService:
    """Servicio para análisis de audio usando APIs externas"""
    
    @staticmethod
    def detect_deepfake(audio_path):
        """
        Detecta si el audio es real o fake usando API externa
        
        Args:
            audio_path (str): Ruta del archivo de audio
            
        Returns:
            dict: Resultado del análisis
        """
        try:
            # Llamada al backend real
            with open(audio_path, 'rb') as audio_file:
                files = {'audio': audio_file}
                url = APIConfig.ML_BACKEND_URL + APIConfig.ML_PREDICT_ENDPOINT
                
                response = requests.post(
                    url,
                    files=files,
                    timeout=APIConfig.RESPONSE_TIMEOUT
                )
                
                if response.status_code == 200:
                    api_data = response.json()
                    
                    # Adaptar respuesta del backend al formato esperado
                    return {
                        'status': 'success',
                        'result': api_data.get('prediction', 'Desconocido'),
                        'confidence': api_data.get('confidence', 0) * 100,
                        'details': {
                            'authenticity': api_data.get('prediction', 'Desconocido'),
                            'probability': api_data.get('confidence', 0),
                            'analysis': api_data.get('message', 'Análisis completado'),
                            'technical_details': api_data.get('details', {})
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
    def identify_speaker(audio_path):
        """
        Identifica al hablante del audio usando API externa
        
        Args:
            audio_path (str): Ruta del archivo de audio
            
        Returns:
            dict: Resultado de la identificación
        """
        try:
            # Llamada al backend real
            with open(audio_path, 'rb') as audio_file:
                files = {'audio': audio_file}
                url = APIConfig.ML_BACKEND_URL + APIConfig.ML_PREDICT_ENDPOINT
                
                response = requests.post(
                    url,
                    files=files,
                    timeout=APIConfig.RESPONSE_TIMEOUT
                )
                
                if response.status_code == 200:
                    api_data = response.json()
                    
                    # Adaptar respuesta del backend al formato esperado
                    speaker_name = api_data.get('speaker', 'Desconocido')
                    confidence = api_data.get('confidence', 0)
                    
                    return {
                        'status': 'success',
                        'result': speaker_name,
                        'confidence': confidence * 100,
                        'details': {
                            'identified': speaker_name != 'Desconocido',
                            'speaker': speaker_name,
                            'probability': confidence,
                            'possible_matches': api_data.get('possible_matches', []),
                            'message': api_data.get('message', 'Análisis completado'),
                            'analysis': api_data.get('analysis', 'Identificación de hablante procesada')
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
        """
        Analiza la calidad del audio
        
        Args:
            audio_path (str): Ruta del archivo de audio
            
        Returns:
            dict: Análisis de calidad
        """
        # Análisis básico de calidad del archivo
        file_size = os.path.getsize(audio_path)
        file_extension = os.path.splitext(audio_path)[1].lower()
        
        return {
            'file_size': file_size,
            'format': file_extension,
            'quality': 'Acceptable' if file_size > 10000 else 'Low'
        }
