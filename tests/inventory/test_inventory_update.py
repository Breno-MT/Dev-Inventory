from flask import json

def test_inventory_create_success(client, logged_in_as_root):
    """ Inventory Product Creation Guide.
    'brand': 'Lazer',
    'description': 'O melhor mouse do mundo serio.',
    'product_category_id': 1,
    'product_code': '984534',
    'template': 'l4zr33r',
    'title': 'Melhor Mouse do Mundo',
    'value': 1231,
    'user_id': OPTIONAL
    """

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
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

    response = client.post('inventory/create', data=json.dumps(data), headers=headers)

    assert response.status_code == 201

def test_inventory_create_same_product_code(client, logged_in_as_root):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
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

    response = client.post('inventory/create', data=json.dumps(data), headers=headers)
    response = client.post('inventory/create', data=json.dumps(data), headers=headers)

    # assert "error" in response.json['error'] == 'Esse código de produto já existe'
    assert response.status_code == 400

def test_inventory_create_missing_body(client, logged_in_as_root):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        'brand': 'Lazerr',
        'description': 'Or melhor mouse do mundo serio.',
        'product_category_id': 1,
        'product_code': '984534',
        'template': 'l4zrr33r',

    }

    response = client.post('inventory/create', data=json.dumps(data), headers=headers)

    assert response.status_code == 400


def test_inventory_create_permission_insufficient(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }

    data = {
        'brand': 'Sim',
        'description': 'Computador para programar',
        'product_category_id': 1,
        'product_code': '981534',
        'template': 'ls11m',
        'title': 'Computador Programação',
        'value': 5000
    }

    response = client.post('inventory/create', data=json.dumps(data), headers=headers)

    assert response.status_code == 403

def test_inventory_create_value_equals_zero(client, logged_in_as_root):
    
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization': f'Bearer {logged_in_as_root}'
    }

    data = {
        'brand': 'Lazerrrrrr',
        'description': 'O melhorrrrrrr mouse do mundo serio.',
        'product_category_id': 1,
        'product_code': '284534',
        'template': 'l4zr33r',
        'title': 'Melhor Mouse do Mundo',
        'value': -12
    }

    response = client.post('inventory/create', data=json.dumps(data), headers=headers)

    assert response.status_code == 400

