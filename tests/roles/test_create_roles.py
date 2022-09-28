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
        "permissions": ["1", "2"]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["message"] == "Role criada com sucesso."
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
        "permissions": ["1", "2"]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Você não tem permissão."
    assert response.status_code == 403


def test_create_role_missing_array_of_permission(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        "description": "Criador de Conteúdo"
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
        "permissions": ["1", "2", "3", "4"]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)
    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Role já existente."
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
        "permissions": ["10", "15"]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Permissões são inválidas."
    assert response.status_code == 400

