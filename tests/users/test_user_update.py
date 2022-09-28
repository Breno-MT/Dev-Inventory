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
