"""Use `pytest` to run this test
"""
import django
from django.test.client import Client

import app  # noqa

django.setup()


def test_django_app():
    client = Client()
    response = client.get('/')
    assert response.content == b'Hello, World!'
