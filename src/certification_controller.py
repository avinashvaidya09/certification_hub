import os
import json
from httpx import Client
from openai import OpenAI
from flask import Flask, request, Blueprint, jsonify
import openai
from werkzeug.wrappers import response
from dotenv import load_dotenv

# Create certification controller blue print
certification_controller_bp = Blueprint('certification_controller', __name__)

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

openai_api_key = os.getenv('OPENAI_API_KEY')


openai_client = OpenAI(api_key=openai_api_key)


@certification_controller_bp.route('/uploadPdf', methods=['POST'])
def uploadPdf():
    intput_question = json.loads(request.data)
    print("Question: ", intput_question);
    return ""


@certification_controller_bp.route('/generateAnswer', methods=['POST'])
def generateAnswer():
    json_payload = request.get_json()
    prompt = json_payload['question']
    print("input to chatgpt: ", prompt)
    try:

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "The content is about geographies and country"},
                {"role": "user", "content": prompt}
            ]
        )
        generateAnswer = response.choices[0].message.content
        print("Response: ", generateAnswer)
        return jsonify({'response': generateAnswer})

    except openai.OpenAIError as e:
        return jsonify({'error': str(e)}), 500