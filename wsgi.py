from flask import Flask
from app.views import api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api, url_prefix='/api/v1')

    return app


if __name__ == '__main__':
    create_app().run()
