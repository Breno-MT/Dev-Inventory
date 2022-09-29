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
        "permissions": [1, 2]
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
        "name": "YouTuber",
        "permissions": [1, 2]
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
        "name": "Se funcionar, deu ruim demais",
        "permissions": [1, 2]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "Permissões são inválidas."
    assert response.status_code == 400


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
        "permission": [1,2,3]
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)

    assert response.json["error"] == "description deve ser apenas String."
    assert response.status_code == 403


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
        "permission": []
    }

    response = client.post("user/role", data=json.dumps(data), headers=headers)


    assert response.json["error"] == "permission não pode ser menor ou igual a 0."
    assert response.status_code == 403


