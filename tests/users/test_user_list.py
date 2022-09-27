from flask import json

def test_list_user(client, logged_in_client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        "Authorization": f"Bearer {logged_in_client}"
    }


    response = client.get("user/", headers=headers)

    assert response.json
