from urllib import response
from flask import json

def test_inventory_list_insufficient_permission(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.get('inventory/', headers=headers)

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

    assert response.status_code == 403

