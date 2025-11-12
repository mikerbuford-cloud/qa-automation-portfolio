# conftest.py
# This file is pytest’s special file where you define shared fixtures and hooks. 
# Pytest auto-discovers it and makes the fixtures available to all tests 
# under the same directory tree without needing explicit imports.
 
 
import pytest
import requests

@pytest.fixture(scope="session") # Session-scoped fixture
def api_base_url():
    # Using ReqRes.in - a real, free API for testing
    # This can later be read from env/CI vars for different environments
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def api_client(api_base_url):
    # Simple wrapped client; can be replaced by a class later
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json"
        # add auth here when ready
    })
    session.base_url = api_base_url
    return session

@pytest.fixture
def user_data():
    return {"name": "Mike", "role": "QA Engineer"}
