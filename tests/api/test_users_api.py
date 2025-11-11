import os
import requests

# Base URL for the ReqRes API used by these tests. Keep trailing path off so
# individual tests can append endpoints and query parameters as needed.
BASE_URL = "https://reqres.in/api"

# Read API key from environment variable to avoid committing secrets.
# This pattern ensures we don't accidentally commit API keys to source control.
API_KEY = os.getenv("REQRES_API_KEY")

# Fail fast if the API key isn't set so tests don't continue with unauthorized
# requests — this makes failures obvious and prevents noisy test runs.
if not API_KEY:
    raise RuntimeError("Set REQRES_API_KEY in the environment to run these tests")

# Common headers sent with every request. The API expects the key in
# the `x-api-key` header for this service.
HEADERS = {"x-api-key": API_KEY}


def test_get_users_status_code():
    """Verify GET /users returns 200 status."""
    url = f"{BASE_URL}/users?page=100"
    
    # Debug: Show what we're about to do
    print(f"\n🔍 DEBUG: Making request")
    print(f"➡️  URL: {url}")
    print(f"➡️  Headers: {HEADERS}")
    
    # Send the request
    response = requests.get(url, headers=HEADERS)
    
    # Debug: Show what we got back
    print(f"\n📥 DEBUG: Got response")
    print(f"⬅️  Status: {response.status_code}")
    print(f"⬅️  Response Headers: {dict(response.headers)}")
    print(f"⬅️  Body Preview: {response.text[:100]}...")
    
    # Run our assertions
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.status_code == 200, f"Status: {response.status_code} URL: {response.url} Body: {response.text[:300]}"


def test_user_not_found():
    """Verify non-existing user returns 404."""
    url = f"{BASE_URL}/users/9999"
    
    # Debug: Show what we're about to do
    print(f"\n🔍 DEBUG: Making request")
    print(f"➡️  URL: {url}")
    print(f"➡️  Headers: {HEADERS}")
    
    # Send the request
    response = requests.get(url, headers=HEADERS)
    
    # Debug: Show what we got back
    print(f"\n📥 DEBUG: Got response")
    print(f"⬅️  Status: {response.status_code}")
    print(f"⬅️  Response Headers: {dict(response.headers)}")
    print(f"⬅️  Body: {response.text}")
    
    # Run our assertions
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

