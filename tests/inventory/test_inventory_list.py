from multiprocessing.context import assert_spawning
import random
from flask import json

def test_inventory_list_insufficient_permission(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.get('inventory/', headers=headers)

    assert response.json["error"] == "Você não tem permissão"
    assert response.status_code == 403


def test_inventory_list_all_success(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }

    response = client.get("inventory/", headers=headers)

    assert response.status_code == 200

def test_inventory_list_by_name_success(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f"Bearer {logged_in_client}"
    }

    name = "Mouse"

    response = client.get(f"inventory/?name={name}", headers=headers)

    assert response.status_code == 200

def test_inventory_list_by_name_no_content(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    name = 'ZZZZZZ'

    response = client.get(f'inventory/?name={name}', headers=headers)

    assert response.status_code == 204

def test_inventory_list_results(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    response = client.get('inventory/results', headers=headers)

    assert response.status_code == 200

def test_inventory_list_results_permission_insufficient(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.get('inventory/results', headers=headers)

    assert response.json["error"] == "Você não tem permissão"
    assert response.status_code == 403

def test_inventory_get_product_by_id_param_success(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    random_id = random.randint(1,5)

    response = client.get(f'inventory/id:{random_id}', headers=headers)

    assert random_id == response.json['id']
    assert response.status_code == 200

def test_inventory_get_product_by_id_param_permission_insufficient(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    random_id = random.randint(1,5)

    response = client.get(f"inventory/id:{random_id}", headers=headers)

    assert response.json["error"] == "Você não tem permissão"
    assert response.status_code == 403


def test_inventory_get_product_by_id_not_found(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    random_id = 300

    response = client.get(f"inventory/id:{random_id}", headers=headers)

    assert response.json["error"] == "Id não existente."
    assert response.status_code == 404

def test_inventory_get_product_by_id_invalid_format(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    random_str = "nãoéprafuncionar"

    response = client.get(f"inventory/id:{random_str}", headers=headers)

    assert response.status_code == 404

def test_inventory_get_product_by_id_no_param_used(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_client}'
    }

    response = client.get("inventory/id:", headers=headers)

    assert response.status_code == 404


