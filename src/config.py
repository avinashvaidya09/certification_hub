import os
from dotenv import load_dotenv
from constants import DOTENV_COMMON_PATH, DOTENV_LOCAL_PATH, DOTENV_DEV_PATH, LOCAL, DEV, ERROR_MESSAGES

def load_environment_variables():
    # Load common environment variables from .env file
    load_dotenv(DOTENV_COMMON_PATH)

    environment = os.getenv('ENVIRONMENT', LOCAL)  # Default to 'local' if ENVIRONMENT is not set

    # Load  environment specific environment variables from .env file
    if environment == LOCAL:
        load_dotenv(DOTENV_LOCAL_PATH, override=True)  
    elif environment == DEV:
        load_dotenv(DOTENV_DEV_PATH, override=True) 

load_environment_variables()

# Load open api key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError(ERROR_MESSAGES['open_api_key_value_error'])