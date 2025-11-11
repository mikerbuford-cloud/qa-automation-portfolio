# test_users_api.py

import pytest
import requests


def test_get_users_returns_200(api_client):
    resp = api_client.get(f"{api_client.base_url}/users")
    assert resp.status_code == 200
    users = resp.json()
    assert isinstance(users, list)
    assert len(users) > 0 