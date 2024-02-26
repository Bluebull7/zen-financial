import os
# config.py

# SQLite database settings
#DATABASE = 'mydatabase.db'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Adjust as needed
}
# Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = 'KCAMF5GEKRVRY995'