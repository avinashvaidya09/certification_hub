import openai
import json
import os
from openai import OpenAI
from flask import jsonify
from constants import ERROR_MESSAGES, PDF_TEMP_STORAGE_PATH, PROMPT_QUESTION
from certification_util import CertificationUtil
from config import openai_api_key

class OpenAiService(object):

    def __init__(self) -> None:
        # Initiate the open ai client
        self.openai_client = OpenAI(api_key=openai_api_key)


    def get_response(self, file):
        extracted_text = ''
        try:
             # Save the file in temporary storage
            file.save(PDF_TEMP_STORAGE_PATH)
             # Extract text from the PDF
            extracted_text = CertificationUtil.extract_text_from_pdf(PDF_TEMP_STORAGE_PATH)

            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": extracted_text},
                {"role": "user", "content": PROMPT_QUESTION}
                ]
            )

            generatedQuestions = response.choices[0].message.content

            if generatedQuestions is None:
                return jsonify({'error': ERROR_MESSAGES['empty_open_ai_response']}), 500

            response_data = json.loads(generatedQuestions)

        except openai.OpenAIError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            if os.path.exists(PDF_TEMP_STORAGE_PATH):
                os.remove(PDF_TEMP_STORAGE_PATH)
            else:
                print(f"File {PDF_TEMP_STORAGE_PATH} does not exist.")
        
        return response_data