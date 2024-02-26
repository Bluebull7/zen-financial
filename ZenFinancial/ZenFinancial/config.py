import os
import dotenv.load_dotenv

# config.py

# SQLite database settings
#DATABASE = 'mydatabase.db'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv.load_dotenv()

api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')



DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Adjust as needed
