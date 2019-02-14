from marshmallow import Schema, fields


class PetSchema(Schema):
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    species = fields.Str(required=True)
    hair_color = fields.Str(required=True)
    owner = fields.Str(required=True)
