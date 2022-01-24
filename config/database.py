import os
from urllib.parse import quote_plus

from flask import current_app


def db_url():
    if os.getenv("DB_CONNECTION") is None:
        # throw an exception
        raise ValueError('Database dialect not specified. DB_CONNECTION should be specified on .env')
   
    if "sqlite" in os.getenv("DB_CONNECTION").lower():
        return ("%s:///%s" % (os.getenv("DB_CONNECTION"),
                              os.path.join(current_app.instance_path, os.getenv('DB_DATABASE'))))
    else:
        return ("%s+%s://%s:%s@%s:%s/%s" % (os.getenv("DB_CONNECTION"),
                                            os.getenv('DB_DRIVER'),
                                            os.getenv('DB_USERNAME'),
                                            quote_plus(os.getenv('DB_PASSWORD')),
                                            os.getenv('DB_HOST'),
                                            os.getenv('DB_PORT'),
                                            os.getenv('DB_DATABASE')))
