import json
from flask import Flask, request, Blueprint, jsonify
from openai_service2 import OpenAiService2
from constants import ERROR_MESSAGES, PDF_TEMP_STORAGE_PATH, PROMPT_QUESTION

# Create certification controller blue print
generate_questions_bp = Blueprint('generate_questions', __name__)


# Method to generate questions from the pdf
@certification_controller_bp.route('/generateQuestions', methods=['POST'])
def generateQuestions():
    chapterString = ""
    try:
       
        # Call OpenAIService
        open_ai_response = OpenAiService2().get_response(request.args.text);

        # Convert the response in JSON format
        response_dto = jsonify(open_ai_response)
    
    except json.JSONDecodeError:
        return jsonify({'error': ERROR_MESSAGES['openai_response_parsing_error']}), 500
    except Exception as e:
            return jsonify({'error': str(e)}), 500
    finally:
        file.close
        
    return response_dto