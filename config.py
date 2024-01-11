import os
from dotenv import load_dotenv

# load environmetn variables
load_dotenv()

#CONSTANTS
API_KEY = os.environ.get("API_KEY")
URL = os.environ.get("URL")