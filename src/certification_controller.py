import os
import json
import PyPDF2
from httpx import Client
from openai import OpenAI
from flask import Flask, request, Blueprint, jsonify
import openai
from werkzeug.wrappers import response
from dotenv import load_dotenv


# Create certification controller blue print
certification_controller_bp = Blueprint('certification_controller', __name__)

def load_environment_variables():
    # Load common environment variables from .env file
    load_dotenv('./resources/.env')

    environment = os.getenv('ENVIRONMENT', 'local')  # Default to 'local' if ENVIRONMENT is not set

    # Load  environment specific environment variables from .env file
    if environment == 'local':
        dotenv_local_path = './resources/.env.local'
        load_dotenv(dotenv_local_path, override=True)  
    elif environment == 'development':
        dotenv_dev_path = './resources/.env.development'
        load_dotenv(dotenv_dev_path, override=True) 

load_environment_variables()

# Load open api key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initiate the open ai client
openai_client = OpenAI(api_key=openai_api_key)

# Method to upload PDF on the server
@certification_controller_bp.route('/uploadPdf', methods=['POST'])
def uploadPdf():
    intput_question = json.loads(request.data)
    print("Question: ", intput_question);
    return ""

# Function to extract text from PDF. Assuming that we are loading only one pdf page
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        if len(reader.pages) > 0:
            page = reader.pages[0]
            text = page.extract_text()
    return text

# Method to generate questions from the pdf
@certification_controller_bp.route('/generateQuestions', methods=['POST'])
def generateQuestions():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    extracted_text = ''

    try:
        # Save the uploaded PDF file temporarily
        pdf_path = './resources/file.pdf'
        file.save(pdf_path)

        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(pdf_path)

    except Exception as e:
            return jsonify({'error': str(e)}), 500


    try:
        prompt="Generate certification questions with options and answers from the text in JSON format to return in REST API response"

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": extracted_text},
                {"role": "user", "content": prompt}
            ]
        )
        generatedQuestions = response.choices[0].message.content

        if generatedQuestions is None:
            return jsonify({'error': 'Response from OpenAI is empty'}), 500

        response_data = json.loads(generatedQuestions)

        return jsonify(response_data)

    except openai.OpenAIError as e:
        return jsonify({'error': str(e)}), 500
    except json.JSONDecodeError:
        return jsonify({'error': 'Failed to parse response from OpenAI'}), 500