import requests

# Base URL for the ReqRes API used by these tests. Keep trailing path off so
# individual tests can append endpoints and query parameters as needed.
BASE_URL = "https://reqres.in/api"

# ReqRes is a free public API that doesn't require authentication.
# We'll use Accept header for consistency with conftest.py fixtures.
HEADERS = {"Accept": "application/json"}


def test_get_users_status_code():
    """Verify GET /users returns 200 status."""
    url = f"{BASE_URL}/users?page=1"
    
    # Debug: Show what we're about to do
    print(f"\n🔍 DEBUG: Making request")
    print(f"➡️  URL: {url}")
    
    # Send the request with consistent headers
    response = requests.get(url, headers=HEADERS)
    
    # Debug: Show what we got back
    print(f"\n📥 DEBUG: Got response")
    print(f"⬅️  Status: {response.status_code}")
    print(f"⬅️  Body Preview: {response.text[:200]}...")
    
    # Run our assertions
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    # Verify response structure
    data = response.json()
    assert "data" in data, "Response should contain 'data' field"
    assert "page" in data, "Response should contain 'page' field"
    assert data["page"] == 1, f"Expected page 1, got {data['page']}"


def test_users_list_pagination():
    """Test that users list supports pagination."""
    # Test page 1
    url1 = f"{BASE_URL}/users?page=1"
    response1 = requests.get(url1, headers=HEADERS)
    
    print(f"\n🔍 DEBUG: Testing pagination page 1")
    print(f"➡️  URL: {url1}")
    print(f"⬅️  Status: {response1.status_code}")
    
    assert response1.status_code == 200, f"Expected 200, got {response1.status_code}"
    data1 = response1.json()
    
    # Test page 2  
    url2 = f"{BASE_URL}/users?page=2"
    response2 = requests.get(url2, headers=HEADERS)
    
    print(f"\n� DEBUG: Testing pagination page 2")
    print(f"➡️  URL: {url2}")
    print(f"⬅️  Status: {response2.status_code}")
    
    assert response2.status_code == 200, f"Expected 200, got {response2.status_code}"
    data2 = response2.json()
    
    # Verify pagination data structure
    assert data1["page"] == 1, f"Expected page 1, got {data1['page']}"
    assert data2["page"] == 2, f"Expected page 2, got {data2['page']}"
    assert data1["total_pages"] == data2["total_pages"], "Both pages should have same total_pages"
    assert len(data1["data"]) > 0, "Page 1 should have data"
    assert len(data2["data"]) > 0, "Page 2 should have data"
    
    # Verify users are different between pages
    user1_ids = {user["id"] for user in data1["data"]}
    user2_ids = {user["id"] for user in data2["data"]}
    assert user1_ids != user2_ids, "Different pages should have different users"


def test_get_single_user():
    """Verify GET /users/{id} returns a valid user."""
    url = f"{BASE_URL}/users/2"
    
    print(f"\n🔍 DEBUG: Making request for single user")
    print(f"➡️  URL: {url}")
    
    response = requests.get(url, headers=HEADERS)
    
    print(f"\n📥 DEBUG: Got response")
    print(f"⬅️  Status: {response.status_code}")
    print(f"⬅️  Body Preview: {response.text[:200]}...")
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "data" in data, "Response should contain 'data' field"
    user = data["data"]
    assert "id" in user, "User should have 'id' field"
    assert "email" in user, "User should have 'email' field"
    assert user["id"] == 2, f"Expected user ID 2, got {user['id']}"

