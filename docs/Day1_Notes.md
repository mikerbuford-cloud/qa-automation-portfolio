Python 3.9.6
Node -v22.20.0
NPM - v10.9.3
git version 2.51.1

Environment variables are stored by the computer’s operating system (like Windows, macOS, or Linux).
    Environment variables are outside messages or settings for programs.
    They help programs know what to do without changing the program itself.
    They’re easy to change, so you don’t have to rewrite your code.
        You can set these varables via terminal
            Ex. export MY_NAME="Alex"
            export FAVORITE_COLOR="Blue"
            python3 script.py
        Or setting in a file like .zshrc or .bash_profile (which are permenant files you can set these variables in with the same export command)


What is `assert`?

- Short answer: `assert` is a built-in Python statement that checks a condition at runtime. If the condition is True the program continues; if it's False Python raises an `AssertionError` and the program (or test) stops.

- Syntax:

```python
assert <condition>, "optional message"
```

- Quick example:

```python
x = 1
assert x == 1, "x should be 1"    # OK
assert x == 2, "x is not 2"      # raises AssertionError with message
```

- Why this matters in tests:
    - Test frameworks like `pytest` use plain `assert` statements. When an `assert` fails, `pytest` shows helpful details (the expected and actual values).
    - Don't run tests with Python optimization (`python -O`) because that removes `assert` checks.

- Classroom-friendly tip: think of `assert` as a safety checkpoint or a "stop and check" sign.
    - Activity: Have students add an `assert` to a small program and then change the input to see the failure message.
