import multiprocessing
import os

from dotenv import load_dotenv

# load .env
load_dotenv()

wsgi_app = "wsgi:create_app()"
bind = f'{os.getenv("FLASK_HOST")}:{os.getenv("FLASK_PORT") or 8000}'
workers = os.getenv('FLASK_WORKERS') or multiprocessing.cpu_count() * 2
reload = os.getenv('FLASK_ENV', 'local') != 'production'
