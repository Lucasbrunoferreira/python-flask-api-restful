from flask_restful import Resource, abort
from flask import Response, request

import json


class BaseController(Resource):

    @staticmethod
    def write_error(msg: str, status_code: int):
        abort(http_status_code=status_code, message=msg)

    @staticmethod
    def write_response(status_code: int, message=None, data=None):
        custom_response = None
        default_type = "application/json"

        if data and not message:
            custom_response = data
        elif message and not data:
            custom_response = {'message': message}

        return Response(
            content_type=default_type,
            mimetype=default_type,
            status=status_code,
            response=json.dumps(custom_response))

    @staticmethod
    def get_body_data():
        return json.loads(request.data)
