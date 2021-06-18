import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env()

try:
    TEST_MODE = env.bool('TEST_MODE')
    DB_NAME = env('DB_NAME')
    DB_USER = env('DB_USER')
    DB_PASSWORD = env('DB_PASSWORD')
    DB_HOST = env('DB_HOST')
    DB_PORT = env('DB_PORT')
except Exception as e:
    print("Production Environment, TEST_MODE=False, getting database details from environment variables")
    TEST_MODE = False
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')

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
