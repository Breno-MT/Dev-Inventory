from flask import json


def test_list_user_success(client, logged_in_client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }


    response = client.get("user/", headers=headers)

    assert response.status_code == 200


def test_list_user_insufficient_permission(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.get('user/', headers=headers)

    assert response.status_code == 403


def test_list_one_user_by_name(client, logged_in_client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }

    name = "L"

    response = client.get(f"user/?name={name}", headers=headers)

    assert response.status_code == 200


def test_list_many_users_by_name(client, logged_in_client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }

    name = "a"

    response = client.get(f"user/?name={name}", headers=headers)

    assert response.status_code == 200


def test_list_user_no_content(client, logged_in_client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }

    name = "ZZZZZZZZZZZZZ"

    response = client.get(f"user/?name={name}", headers=headers)

    assert response.status_code == 204



