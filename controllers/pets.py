from flask import current_app
from http import HTTPStatus
from marshmallow import ValidationError

from util.common_base import BaseController
from persistence.schemas.pet import PetSchema
from util import data_formatter

from logzero import logger


class PetsController(BaseController):
    pets_collection: None

    def __init__(self):
        current_app.config["mongo"].define_collection('pets')
        self.pets_collection = current_app.config["mongo"]

    def get(self, **kwargs):
        pet_id = kwargs.get('pet_id')
        if pet_id:
            try:
                response = self.pets_collection.find_one(document_id=pet_id)
                pet_data = data_formatter.object_id(data=response)
            except ValueError as ex:
                logger.error(ex)
                raise self.write_error(status_code=HTTPStatus.BAD_REQUEST,
                                       msg='no pet found with id {}'.format(pet_id))
            except Exception as ex:
                logger.error(ex)
                raise self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                       msg=str(ex))
            else:
                return self.write_response(status_code=HTTPStatus.OK,
                                           data=pet_data)
        else:
            try:
                response = self.pets_collection.find_all()
                all_pets_data = data_formatter.object_id(data=response)
            except Exception as ex:
                logger.error(ex)
                raise self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                       msg=str(ex))
            else:
                return self.write_response(status_code=HTTPStatus.OK,
                                           data=all_pets_data)

    def post(self):
        try:
            new_user = PetSchema().load(self.get_body_data())

        except ValidationError as err:
            logger.error(err)
            raise self.write_error(status_code=HTTPStatus.BAD_REQUEST,
                                   msg=str(err))
        else:
            try:
                response = self.pets_collection.insert_one(data=new_user)
            except Exception as ex:
                logger.error(ex)
                raise self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                       msg=str(ex))
            else:
                new_user = self.pets_collection.find_one(document_id=response)
                formatted_new_user = data_formatter.object_id(data=new_user)
                return self.write_response(status_code=HTTPStatus.CREATED,
                                           data=formatted_new_user)

    def put(self, **kwargs):
        pet_id = kwargs.get('pet_id')
        try:
            PetSchema().load(self.get_body_data())

        except ValidationError as err:
            logger.error(err)
            raise self.write_error(status_code=HTTPStatus.BAD_REQUEST,
                                   msg=str(err))
        else:
            try:
                response = self.pets_collection.update_one(document_id=pet_id,
                                                           document=self.get_body_data())

                updated_pet = data_formatter.object_id(data=response)
            except ValueError:
                raise self.write_error(status_code=HTTPStatus.BAD_REQUEST,
                                       msg='no pet found with id {}'.format(pet_id))
            except Exception as ex:
                logger.error(ex)
                raise self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                       msg=str(ex))
            else:
                return self.write_response(status_code=HTTPStatus.OK,
                                           data=updated_pet)

    def delete(self, **kwargs):
        pet_id = kwargs.get('pet_id')
        try:
            self.pets_collection.delete_one(document_id=pet_id)
        except ValueError:
            raise self.write_error(status_code=HTTPStatus.BAD_REQUEST,
                                   msg='no pet found with id {}'.format(pet_id))
        except Exception as ex:
            logger.error(ex)
            raise self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                   msg=str(ex))
        else:
            return self.write_response(status_code=HTTPStatus.OK,
                                       message='the pet was successfully deleted')
