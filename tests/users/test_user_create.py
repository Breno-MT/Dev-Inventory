import random
from flask import json

def test_create_user_permission_insufficient(client, logged_in_client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    headers["Authorization"] = f"Bearer {logged_in_client}"

    data = {
        "email": "teste@gmail.com",
        "city_id": 1,
        "name": "TESTE",
        "age": 12,
        "password": "123345Teste!"
    }

    response = client.post("/user/create", data=json.dumps(data), headers=headers)
    assert response.json["error"] == "Você não tem permissão para essa funcionalidade"
    assert response.status_code == 403


def test_create_user_with_permission(client, logged_in_as_root):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    headers["Authorization"] = f"Bearer {logged_in_as_root}"

    data = {
        "gender_id": 1,
        "city_id": 2,
        "role_id": 1,
        "email": "teste1@gmail.com",
        "city_id": 1,
        "name": "TESTE",
        "age": "1992-02-02",
        "password": "12345678!",
        "cep": "99999999",
        "phone": "99999999999",
        "complement": "Teste N",
        "landmark": "Teste N",
        "district": "Teste N",
        "street": "Rua teste",
        "number_street": "119",
        "complement": "Teste N"
    }

    response = client.post("/user/create", data=json.dumps(data), headers=headers)
    assert response.json['message'] == 'Usuário criado com sucesso.'
    assert response.status_code == 201

def test_create_missing_fields(client, logged_in_as_root):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    headers["Authorization"] = f"Bearer {logged_in_as_root}"

    data = {
        "gender_id": 1,
        "city_id": 2,
        "role_id": 1,
        "email": "teste1@gmail.com",
        "city_id": 1,
        "name": "TESTE",
        "phone": "99999999999",
        "password": "123345Teste!",
        "age": "1992-02-02"
    }

    response = client.post("/user/create", data=json.dumps(data), headers=headers)

    for missing_key in response.json:
        assert response.json[missing_key] == [f'O campo {missing_key} é obrigatório.']

    assert response.status_code == 400


def teste_create_user_with_same_email(client, logged_in_as_root):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    headers["Authorization"] = f"Bearer {logged_in_as_root}"

    data = {
        "gender_id": 1,
        "city_id": 2,
        "role_id": 1,
        "email": "teste1@gmail.com",
        "city_id": 1,
        "name": "TESTE",
        "age": "1992-02-02",
        "password": "123345Teste!",
        "cep": "99999999",
        "phone": "99999999000",
        "complement": "Teste N",
        "landmark": "Teste N",
        "district": "Teste N",
        "street": "Rua teste",
        "number_street": "119",
        "complement": "Teste N"
    }

    response = client.post("/user/create", data=json.dumps(data), headers=headers)
    response = client.post("/user/create", data=json.dumps(data), headers=headers)
    assert response.json["error"] == "Erro na criação de Usuário. Email já existe."
    assert response.status_code == 400
