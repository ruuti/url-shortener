import json
from chalice.test import Client
from app import app


def test_create_link():
    with Client(app) as client:
        url = 'https://url.com'
        response = client.http.post(
            '/',
            headers={'Content-Type': 'application/json'},
            body=json.dumps({'url': url})
        )
        assert response.status_code == 200


def test_create_invalid_link():
    with Client(app) as client:
        url = 'not_valid_url'
        response = client.http.post(
            '/',
            headers={'Content-Type': 'application/json'},
            body=json.dumps({'url': url})
        )
        assert response.status_code == 400


def test_get_link():
    with Client(app) as client:
        url = 'https://url.com'
        response = client.http.post(
            '/',
            headers={'Content-Type': 'application/json'},
            body=json.dumps({'url': url})
        )

        id = response.json_body['id']

        link_response = client.http.get(
            '/' + id
        )

        assert link_response.json_body['url'] == url


def test_invalid_link():
    with Client(app) as client:
        response = client.http.get(
            '/ID_ThAT_DoEs_NoT_eXsIsT'
        )

        assert response.status_code == 404
