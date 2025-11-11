import pytest
import requests
import json


def debug_http_response(response: requests.Response, label: str = "") -> None:
    """Print a concise, readable snapshot of an HTTP response.

    Shows request method+URL, status code, a few headers, and a pretty-printed
    body (JSON if available, otherwise text snippet). Keep output short so it's
    useful in CI logs. Call this inside your tests right after the request.
    """
    req = response.request
    print(f"\n[HTTP] {label} {req.method} {response.url}")
    print(f"[HTTP] status={response.status_code}")
    # Show a small subset of headers to avoid noisy logs
    important_headers = {k: response.headers[k] for k in list(response.headers)[:5]}
    print(f"[HTTP] headers~5={important_headers}")
    try:
        data = response.json()
        print("[HTTP] json=\n" + json.dumps(data, indent=2)[:1000])
    except ValueError:
        print("[HTTP] text=\n" + (response.text or "")[:1000])

@pytest.fixture
def api_client():
    print("[Setup] Logging into API...")
    token = "xyz-123"
    client = {
        "url": "https://jsonplaceholder.typicode.com",  # public dummy API
        "token": token
    }
    yield client
    print("[Teardown] Logging out / Revoking token...")

def test_user_profile(api_client):
    # This test is intended to validate a user profile resource (a single user)
    # The `/users/1` endpoint returns a JSON object (a dict), not a list of posts.
    # We verify the response status, expected keys, and some field values.
    print("\n[Test] Sending GET request to /users/1 ...")
    response = requests.get(f"{api_client['url']}/users/1")
    debug_http_response(response, label="GET /users/1")

    # Basic HTTP success check
    assert response.status_code == 200, (
        f"Unexpected status {response.status_code} for {response.url}. "
        f"Body snippet: {(response.text or '')[:300]}"
    )

    # Make sure the returned JSON contains expected user fields
    user = response.json()
    assert isinstance(user, dict), (
        "Expected a single user object (dict) from /users/1. "
        f"Got type={type(user)} with body={(response.text or '')[:200]}"
    )
    assert "username" in user, f"Missing 'username' in user payload: {user}"

    # Additional sanity checks: id matches requested user and name exists
    assert user.get("id") == 1, f"Expected id=1, got id={user.get('id')}"
    assert user.get("name"), "Expected non-empty 'name' field"


def test_get_posts(api_client):
    print("\n[Test] Running test_get_posts...")
    url = f"{api_client['url']}/posts"
    headers = {"Authorization": f"Bearer {api_client['token']}"}
    response = requests.get(url, headers=headers)
    debug_http_response(response, label="GET /posts")
    assert response.status_code == 200, (
        f"Unexpected status {response.status_code} for {response.url}. "
        f"Body snippet: {(response.text or '')[:300]}"
    )
    posts = response.json()
    print(f"[Debug] Number of posts retrieved: {len(posts)}")
    assert isinstance(posts, list), f"Expected list, got {type(posts)}"
    assert len(posts) > 0, "Expected at least one post"


def test_get_post_by_id(api_client):
    print("\n[Test] Running test_get_post_by_id...")
    post_id = 1
    url = f"{api_client['url']}/posts/{post_id}"
    headers = {"Authorization": f"Bearer {api_client['token']}"}
    response = requests.get(url, headers=headers)
    debug_http_response(response, label=f"GET /posts/{post_id}")
    assert response.status_code == 200, (
        f"Unexpected status {response.status_code} for {response.url}. "
        f"Body snippet: {(response.text or '')[:300]}"
    )
    post = response.json()
    print(f"[Debug] Retrieved Post: {post}")
    assert post.get("id") == post_id, f"Expected id={post_id}, got {post.get('id')}"
               