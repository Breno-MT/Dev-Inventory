import random
from flask import json

def test_inventory_update_product_permission_insufficient(client):

    mimetype = 'application/json'

    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }

    data = {
        'brand': 'Lazer',
        'description': 'O melhor mouse do mundo serio.',
        'product_category_id': 1,
        'product_code': '984534',
        'template': 'l4zr33r',
        'title': 'Melhor Mouse do Mundo',
        'value': 1231
    }

    random_id = random.randint(1,4)

    response = client.patch(f'inventory/{random_id}', data=json.dumps(data), headers=headers)

    assert response.status_code == 403

def test_inventory_update_product_success(client, logged_in_as_root):

    mimetype = 'application/json'

    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        'brand': 'Updated Mouse',
        'description': 'O melhor mouse do mundo updated.',
        'template': 'upd44t3',
        'title': 'Melhor Mouse do Mundo Updated',
        'value': 15000
    }

    random_id = random.randint(1,5)

    response = client.patch(f'inventory/{random_id}', data=json.dumps(data), headers=headers)

    assert response.status_code == 204

def test_inventory_update_product_validate_exception_product_code_and_product_category_id(client, logged_in_as_root):
    
    mimetype = 'application/json'

    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        'brand': 'Updated Mouse',
        'description': 'O melhor mouse do mundo updated.',
        'product_category_id': 1,
        'product_code': '984534',
        'template': 'upd44t3',
        'title': 'Melhor Mouse do Mundo Updated',
        'value': 150200
    }

    random_id = random.randint(1,5)

    response = client.patch(f'inventory/{random_id}', data=json.dumps(data), headers=headers)

    assert response.status_code == 400

