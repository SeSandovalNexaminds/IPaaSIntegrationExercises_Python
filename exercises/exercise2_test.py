
from exercise2 import call_with_retry, reset_state, _counter
import exercise2

def setup_function():
    reset_state()

def test_succeeds_after_retries():
    result = call_with_retry()
    assert result["success"] is True
    assert result["data"]["id"] == 42
    assert _counter == 3

def test_duplicate_id_returns_null_data():
    first = call_with_retry()
    assert first["success"] is True

    second = call_with_retry()
    assert second["success"] is True
    assert second["data"] is None
    assert second["message"] == "Duplicate ignored"

def test_fails_after_all_attempts():
    exercise2._counter = 9999
    result = call_with_retry()
    assert result["success"] is False
    assert result["error"] == "API failed after 3 attempts"
