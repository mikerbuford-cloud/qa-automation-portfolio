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



# tests/conftest.py


# ---- Day-2 auth demo: tiny fake client + tokens ----
class AuthError(Exception):
    """Raised when authentication fails (invalid/expired token)."""
    def __init__(self, message):
        super().__init__(message)
        print(f"[DEBUG] 🚨 EXCEPTION CREATED: AuthError('{message}')")

class FakeApiClient:
    def __init__(self, base_url: str):
        print(f"[DEBUG] 🏗️  CLASS INIT: FakeApiClient.__init__(base_url='{base_url}')")
        self.base_url = base_url
        print(f"[DEBUG] 📝 CLASS STATE: FakeApiClient.base_url = '{self.base_url}'")

    def get_profile(self, token: str):
        print(f"\n[DEBUG] 🎯 METHOD CALL: FakeApiClient.get_profile(token='{token}')")
        print(f"[DEBUG] 🔍 METHOD LOGIC: Evaluating token value...")
        
        # SUPER simplified demo logic for Day 2
        if token == "VALID":
            result = {"name": "Mike", "country": "US"}
            print(f"[DEBUG] ✅ METHOD SUCCESS: Token '{token}' is valid, returning profile data")
            print(f"[DEBUG] 📤 METHOD RETURN: {result}")
            return result
        
        if token == "EXPIRED":
            print(f"[DEBUG] ⏰ METHOD ERROR: Token '{token}' is expired, raising AuthError")
            raise AuthError("expired token")
        
        print(f"[DEBUG] ❌ METHOD ERROR: Token '{token}' is invalid, raising AuthError")
        raise AuthError("invalid token")

# ---- Mock API Testing Fixtures ----
@pytest.fixture
def fake_api_base_url():
    """Fake API base URL for unit testing with mock client"""
    return "https://api.example.test"

@pytest.fixture
def fake_api_client(fake_api_base_url):
    """Fake API client for testing authentication flows without real HTTP calls"""
    print(f"\n[DEBUG] 🔧 FIXTURE SETUP: Creating FakeApiClient with base_url: {fake_api_base_url}")
    client = FakeApiClient(fake_api_base_url)
    print(f"[DEBUG] 📦 FIXTURE DATA: FakeApiClient ready for testing auth scenarios")
    return client

# ---- Authentication Token Fixtures ----
@pytest.fixture
def valid_token():
    return "VALID"

@pytest.fixture
def invalid_token():
    return "BAD"     # not recognized by FakeApiClient

@pytest.fixture
def expired_token():
    return "EXPIRED"
