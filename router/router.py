import os
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename
from services import AudioAnalysisService
from api_config import APIConfig

main_routes = Blueprint('main_routes', __name__)
UPLOAD_FOLDER = APIConfig.UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in APIConfig.ALLOWED_AUDIO_EXTENSIONS

@main_routes.route('/api/analyze', methods=['POST'])
def analyze_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No se encontró ningún archivo de audio'
            }), 400
        
        file = request.files['audio']
        action = request.form.get('action', 'detect')
        
        if file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No se seleccionó ningún archivo'
            }), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'status': 'error',
                'message': 'Formato de archivo no permitido. Use: wav, mp3, ogg, flac, m4a, aac'
            }), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        quality_info = AudioAnalysisService.analyze_audio_quality(filepath)
        
        if action == 'detect':
            api_result = AudioAnalysisService.detect_deepfake(filepath)
            
            if 'error' in api_result:
                return jsonify({
                    'status': 'error',
                    'message': api_result.get('message', api_result['error'])
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
            api_result = AudioAnalysisService.identify_speaker(filepath)
            
            if 'error' in api_result:
                return jsonify({
                    'status': 'error',
                    'message': api_result.get('message', api_result['error'])
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
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error al procesar el archivo: {str(e)}'
        }), 500


@main_routes.route('/api/hello')
def api_hello():
    return jsonify({'mensaje': 'Hola desde la API', 'status': 'success'})

@main_routes.route('/api/convert-wav', methods=['POST'])
def convert_to_wav():
    try:
        if 'audio' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No se encontró ningún archivo de audio'
            }), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No se seleccionó ningún archivo'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'status': 'error', 'message': 'Formato de archivo no permitido'}), 400
        
        filename = secure_filename(file.filename)
        original_name = os.path.splitext(filename)[0]
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(UPLOAD_FOLDER, f"{original_name}_converted.wav")
        file.save(input_path)
        
        try:
            from pydub import AudioSegment
            audio = AudioSegment.from_file(input_path)
            audio.export(output_path, format='wav')
            return send_file(output_path, as_attachment=True, download_name=f"{original_name}.wav", mimetype='audio/wav')
            
        except ImportError:
            return jsonify({'status': 'error', 'message': 'Librería de conversión no disponible. Instala pydub y ffmpeg.'}), 500
        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Error al convertir: {str(e)}'}), 500
        finally:
            try:
                if os.path.exists(input_path):
                    os.remove(input_path)
                if os.path.exists(output_path):
                    os.remove(output_path)
            except:
                pass
                
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error en el servidor: {str(e)}'
        }), 500


@main_routes.route('/api/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    return jsonify({'recibido': datos, 'mensaje': 'Datos procesados correctamente'})

