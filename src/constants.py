# Context to send to the open ai model
PROMPT_QUESTION='Generate certification questions with options and answers from the text in JSON format to return in REST API response'

# Paths
DOTENV_COMMON_PATH = './resources/.env'
DOTENV_LOCAL_PATH = './resources/.env.local'
DOTENV_DEV_PATH = './resources/.env.development'
PDF_TEMP_STORAGE_PATH = './resources/file.pdf'

# Environments
LOCAL='local'
DEV='development'

# Error Messages
ERROR_MESSAGES = {
    'open_api_key_value_error': 'The OpenAI API key is not set. Please check your .env file and environment variables.',
    'no_file_to_parse': 'No file part in the request',
    'no_file_selected': 'No selected file',
    'empty_open_ai_response': 'Response from OpenAI is empty',
    'openai_response_parsing_error': 'Failed to parse response from OpenAI'
}