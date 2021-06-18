import os
import warnings

import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
with warnings.catch_warnings(record=True) as w:
    environ.Env.read_env()

env_file_is_missing = True if len(w) == 1 else False

DEBUG = os.environ.get('DEBUG', False) if env_file_is_missing else env.bool('DEBUG')

print("No .env file found under core/settings. Attempting to get sensitive info from production server environment variables") if env_file_is_missing else None
TEST_MODE = False if env_file_is_missing else env.bool('TEST_MODE')
DB_NAME = os.environ.get('DB_NAME') if env_file_is_missing else env('DB_NAME')
DB_USER = os.environ.get('DB_USER') if env_file_is_missing else env('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD') if env_file_is_missing else env('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST') if env_file_is_missing else env('DB_HOST')
DB_PORT = os.environ.get('DB_PORT') if env_file_is_missing else env('DB_PORT')

if DB_NAME is None:
    print("Currently no .env file exists to get the environment variables from under core/settings folder. The variables are not defined as an environment variable on the server either.")
    raise SystemExit

if TEST_MODE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
