from flask import Flask
from werkzeug.exceptions import HTTPException

from app.views import api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api, url_prefix='/api/v1')

    @app.errorhandler(404)
    def not_found_error_handler(e):
        return {'error': 'Not found'}, 404

    @app.errorhandler(Exception)
    def generic_error_handler(e):
        if isinstance(e, HTTPException):
            if e.get_response().is_json:
                return e
            else:
                e.response.content_type = 'application/json'
                return e
        return {'error': 'Internal server error'}, 500

    return app


if __name__ == '__main__':
    create_app().run()
