from marshmallow import Schema, fields, ValidationError, validates
from src.app.utils.error_messages import handle_error_messages

def func_validate_name(name):
    if len(name) <= 5 and not isinstance(name, str):
        raise ValidationError("name deve ser apenas String e acima de 5 caracteres.")
    
    if len(name) <= 5 and isinstance(name, str):
        raise ValidationError("name deve ser apenas String e acima de 5 caracteres.")


def func_validate_description(description):
    if len(description) <= 5 and not isinstance(description, str):
        raise ValidationError('description deve ser apenas String e acima de 5 caracteres.')
    
    if len(description) <= 5 and isinstance(description, str):
        raise ValidationError('description deve ser apenas String e acima de 5 caracteres.')


class CreaterRoleSchema(Schema):
    description = fields.String(required=True, error_messages=handle_error_messages('description'))
    name = fields.String(required=True, error_messages=handle_error_messages('name'))
    permissions = fields.List(fields.Integer(), required=True, error_messages=handle_error_messages('permissions'))

    @validates('description')
    def validate_description(self, description):
        func_validate_description(description)
    
    @validates('name')
    def validate_name(self, name):
        func_validate_name(name)

    @validates('permissions')
    def validate_permission(self, permissions):
        # Aqui é só para saber se o Length[Array] da Permission é maior que 0, caso sim, a controller faz a outra verificação se existe ou não
        # as permissões no banco de dados. 
        if len(permissions) <=0:
            raise ValidationError('O permissions não pode ser menor ou igual a 0.')

