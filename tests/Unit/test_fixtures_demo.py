# Import the pytest module which provides the testing framework and fixture functionality
import pytest

# Define a pytest fixture named 'user_data'
# Fixtures are used to provide a fixed baseline for tests
# They can set up test data, create connections, or prepare any other test prerequisites
@pytest.fixture
def user_data():
    print("\n[DEBUG] 🔧 FIXTURE SETUP: Starting user_data fixture setup...")
    
    # Create the test data
    data = {"name": "Mike", "role": "QA Engineer"}
    print(f"[DEBUG] 📦 FIXTURE DATA: Created user data: {data}")
    
    # This yield statement means this is a generator fixture
    # The code after yield runs after all tests using this fixture complete
    yield data
    print("[DEBUG] 🧹 FIXTURE CLEANUP: user_data fixture is being cleaned up")

# Test function that uses the user_data fixture
# Pytest automatically passes the fixture's return value to the test function
def test_user_name(user_data):
    print(f"\n[DEBUG] 🏃 TEST START: Running test_user_name with data: {user_data}")
    
    # Get the actual value we're testing
    actual_name = user_data["name"]
    print(f"[DEBUG] 👤 TEST DATA: Checking name: '{actual_name}'")
    
    # Assert that the user's name matches the expected value
    # If this assertion fails, pytest will show the actual vs expected values
    assert actual_name == "Mike"
    print("[DEBUG] ✅ TEST RESULT: Name assertion passed!")

# Another test function using the same fixture
# This demonstrates fixture reuse - the fixture runs once and its value is shared
def test_user_role(user_data):
    print(f"\n[DEBUG] 🏃 TEST START: Running test_user_role with data: {user_data}")
    
    # Get the actual value we're testing
    actual_role = user_data["role"]
    expected_role = "qa engineer"
    print(f"[DEBUG] 👥 TEST DATA: Checking role: '{actual_role}' against '{expected_role}' (case-insensitive)")
    
    # Assert that the user's role matches "qa engineer" (case-insensitive)
    # Using lower() makes this comparison case-insensitive
    assert actual_role.lower() == expected_role
    print("[DEBUG] ✅ TEST RESULT: Role assertion passed!") 
