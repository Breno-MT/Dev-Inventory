from flask import json

def test_create_role_success(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Criador de Conteúdo",
        "name": "YouTuber",
        "permissions": [1, 2, 3, 4]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)


    assert response.status_code == 201


def test_create_role_permission_insufficient(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    data = {
        "description": "Criador de Conteúdo",
        "name": "YouTuber",
        "permissions": [1, 2]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Você não tem permissão para essa funcionalidade"
    assert response.status_code == 403


def test_create_role_missing_array_of_permission(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Criador de Conteúdo",
        "name": "YouTuber"
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == [f'O campo {error} é obrigatório.']
    
    assert response.status_code == 400


def test_create_role_already_exists(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Brabo",
        "name": "O mais brabo",
        "permissions": [1, 2, 3, 4]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)
    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Erro na criação de Role. Role já existente."
    assert response.status_code == 400


def test_create_role_with_non_existent_permission(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Teste",
        "name": "Se funcionar, deu ruim demais",
        "permissions": [5, 5]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Array de Permissões não existente."
    assert response.status_code == 404

def test_create_role_with_non_existent_and_existent_permissions(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Teste",
        "name": "Se funcionar, deu ruim demais",
        "permissions": [1, 5, 6, 2, 10, 12, 3]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == 'Array de Permissões não existente.'
    assert response.status_code == 404


def test_create_role_with_invalid_description_format(client, logged_in_as_root):
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    data = {
        "description": 1234,
        "name": "1234",
        "permissions": [1,2,3]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == [f'{error} Não é um campo válido.']

    assert response.status_code == 400


def teste_create_role_with_zero_permissions(client, logged_in_as_root):
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype,
        "Authorization": f"Bearer {logged_in_as_root}"
    }

    data = {
        "description": "Melhor Teste já realizado",
        "name": "De fato é o melhor",
        "permissions": []
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    for error in response.json:
        assert response.json[error] == [f'O {error} não pode ser menor ou igual a 0.']
    
    assert response.status_code == 400


