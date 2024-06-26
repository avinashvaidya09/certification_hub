import json
from flask import Flask, request, Blueprint, jsonify
from openai_service import OpenAiService
from constants import ERROR_MESSAGES, PDF_TEMP_STORAGE_PATH, PROMPT_QUESTION

# Create certification controller blue print
certification_controller_bp = Blueprint('certification_controller', __name__)


# Method to generate questions from the pdf
@certification_controller_bp.route('/generateQuestions', methods=['POST'])
def generateQuestions():
    if 'file' not in request.files:
        return jsonify({'error': ERROR_MESSAGES['no_file_to_parse']}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': ERROR_MESSAGES['no_file_selected']}), 400
    
    try:
       
        # Call OpenAIService
        open_ai_response = OpenAiService().get_response(file);

        # Convert the response in JSON format
        response_dto = jsonify(open_ai_response)
    
    except json.JSONDecodeError:
        return jsonify({'error': ERROR_MESSAGES['openai_response_parsing_error']}), 500
    except Exception as e:
            return jsonify({'error': str(e)}), 500
    finally:
        file.close
        
    return response_dto