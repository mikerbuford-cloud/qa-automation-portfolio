Fixtures
Think of a fixture as a “setup assistant.”
It’s a function that prepares data, state, or resources that your test needs before it runs.

Instead of repeating setup logic (like connecting to a database, creating test users, or loading config), you put it in a fixture once, then reuse it across multiple tests.

Fixtures gives you access to Automate the following process
    1. Set something up (e.g., create a user, connect to DB, open browser).
    2. Run your test.
    3. Tear it down (e.g., delete user, close DB, quit browser).


Why Fixtures Matter for QE Work

As a Quality Engineer, fixtures are one of your most valuable tools because:

    You can simulate different environments (staging vs prod).

    You can generate mock API responses or test data for automated UI flows.

    You can isolate test setup logic from the test itself, keeping tests short and clear.

The YIELD fixture
Setup and Breakdown
When Pytest sees yield, it splits the function into two phases:

    Everything before yield runs before the test (setup).

    Everything after yield runs after the test (teardown).

That means Pytest:

    Pauses the fixture at yield.

    Executes your test using the value you yielded.

    Resumes the fixture after the test to clean up.

Conftest.py
    “conftest.py is pytest’s way to share fixtures across multiple test files without explicit imports.”

Assertions
Type & Structure
“I add type/shape assertions so tests fail early if the API or data model changes (e.g., name becomes None or an int). This catches regressions that equality alone wouldn’t.”

Type -  Is the field the right kind of thing
Type Ex. 
    assert isinstance(user_data["name"], str)

Key/Shape - Does the object have the fields we require?
Key Ex.
    required = {"name", "role"}
    assert required.issubset(user_data.keys())

Len/format check — is it “stringy” but also non-empty or formatted?
Len Ex. 
    assert isinstance(user_data["role"], str) and user_data["role"].strip() != ""