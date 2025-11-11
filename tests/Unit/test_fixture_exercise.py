# Import pytest for our testing framework
import pytest

# Define a fixture that provides a sample user for our tests
# This fixture uses yield, which allows for setup and cleanup phases
@pytest.fixture
def sample_user():
    print("\n[DEBUG] 🔧 FIXTURE SETUP: Creating sample user fixture...")
    
    # Create our test user data
    user_data = {"id": 42, "name": "Max", "active": True}
    print(f"[DEBUG] 📦 FIXTURE DATA: Created user: {user_data}")
    
    # yield suspends the fixture function here and returns the data
    # tests will run with this data, then execution returns here for cleanup
    yield user_data
    
    # This code runs after all tests using this fixture complete
    print("[DEBUG] 🧹 FIXTURE CLEANUP: Cleaning up sample user resources...")

# Test to verify the user's active status
# Uses the sample_user fixture which provides the test data
def test_user_is_active(sample_user):
    print(f"\n[DEBUG] 🏃 TEST START: Running test_user_is_active with user: {sample_user}")
    
    # Get the active status we're testing
    is_active = sample_user["active"]
    print(f"[DEBUG] 👤 TEST DATA: Checking active status: {is_active}")
    
    # Assert that the user is active (active flag should be True)
    assert is_active, "User should be active"
    print("[DEBUG] ✅ TEST RESULT: User active status verified!")

# Test to verify the user ID is the correct type
# Also uses the sample_user fixture, demonstrating fixture reuse
def test_user_has_id(sample_user):
    print(f"\n[DEBUG] 🏃 TEST START: Running test_user_has_id with user: {sample_user}")
    
    # Get the ID we're testing
    user_id = sample_user["id"]
    print(f"[DEBUG] 🔢 TEST DATA: Checking user ID type: {user_id} (type: {type(user_id)})")
    
    # Assert that the ID is an integer
    assert isinstance(user_id, int), f"User ID should be an integer, got {type(user_id)}"
    print("[DEBUG] ✅ TEST RESULT: User ID type verified!")
