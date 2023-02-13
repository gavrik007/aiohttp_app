from marshmallow import Schema, fields
from app.web.schemes import OkResponseSchema


class UserAddSchema(Schema):
    email = fields.Str(required=True)


class UserSchema(UserAddSchema):
    id = fields.UUID(required=True, attribute="id_")


class UserGetRequestSchema(Schema):
    id = fields.UUID(required=True)


class UserGetSchema(Schema):
    user = fields.Nested(UserSchema())


class UserGetResponseSchema(OkResponseSchema):
    data = fields.Nested(UserGetSchema())


class ListUserSchema(Schema):
    users = fields.Nested(UserSchema(), many=True)


class ListUserResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUserSchema())
