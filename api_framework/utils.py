import json
import os
from dotenv import load_dotenv

load_dotenv()

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_base_url():
    return os.getenv("BASE_URL")

