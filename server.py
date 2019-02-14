from flask import Flask
from flask_restful import Api

from controllers.pets import PetsController
from persistence.database.mongo import MongoDb

import settings

app = Flask(__name__)
service = Api(app)

api_version = 1

service.add_resource(PetsController,
                     '/api/v{}/pets'.format(api_version),
                     '/api/v{}/pets/<string:pet_id>'.format(api_version))

if __name__ == '__main__':
    settings.config_logs()
    app.config["mongo"] = MongoDb()
    app.run(debug=True, port=settings.APP_PORT)
