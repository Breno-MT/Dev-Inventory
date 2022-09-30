import random
from flask import json

def test_update_user_success(client, logged_in_as_root):
    
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "123TEstando!!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    assert response.status_code == 204

def test_update_user_permission_insufficient(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "123TEstando!!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    assert response.json['error'] == 'Você não tem permissão'
    assert response.status_code == 403

def test_update_user_with_empty_body(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "",
        "name": "teste",
        "password": "123TEstando!!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == [f'{error} Não é um campo válido.']

    assert response.status_code == 400

def test_update_user_not_found(client, logged_in_as_root):
    
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(100,900)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "123TEstando!!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    assert response.json['error'] == 'Usuário não existe.'
    assert response.status_code == 404

def test_update_user_invalid_password_length(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "12"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for password in response.json:
        assert response.json[password] == ['A senha precisa ser maior ou igual a 8.']

    assert response.status_code == 400

def test_update_user_missing_symbol_password(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "123456789"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for password in response.json:
        assert response.json[password] == ['A senha precisa ter pelo menos 1 caracter especial.']

    assert response.status_code == 400

def test_update_user_invalid_email(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111gmail.com",
        "name": "TESTE",
        "password": "12345Teste!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for email in response.json:
        assert response.json[email] == [f'{email} Não é um campo válido.']

    assert response.status_code == 400

def test_update_user_patch_wrong_fields(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    user_id = random.randint(1,8)

    data = {
        "email": "teste1111@gmail.com",
        "name": "TESTE",
        "password": "123TEstando!!",
        "naosei": "sotestando"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == [f'Unknown field.']

    assert response.status_code == 400

def test_update_user_patch_same_email(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f"Bearer {logged_in_as_root}"
    }

    user_id = 12

    data = {
        "email": "luislopes@gmail.com",
        "name": "TESTE",
        "password": "123TEstando!!"
    }

    response = client.patch(f"user/{user_id}", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == 'Email já existe.'
    
    assert response.status_code == 409

