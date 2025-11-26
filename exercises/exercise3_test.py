
from exercise3 import process_events

def test_sort_and_dedupe():
    result = process_events([
        {"event_id": 5, "type": "x", "timestamp": 300, "payload": {"a": 1}},
        {"event_id": 5, "type": "y", "timestamp": 100, "payload": {"a": 2}},
    ])

    assert len(result["validEvents"]) == 1
    assert result["validEvents"][0]["timestamp"] == 100
    assert result["validEvents"][0]["payload"] == {"a": 2}

def test_missing_payload_goes_to_invalid():
    result = process_events([
        {"event_id": 1, "type": "create", "timestamp": 100},
        {"event_id": 2, "type": "create", "timestamp": 200, "payload": {"id": 1}},
    ])

    assert len(result["validEvents"]) == 1
    assert len(result["invalidEvents"]) == 1
    assert result["invalidEvents"][0] == {
        "event_id": 1,
        "reason": "Missing payload",
    }

def test_missing_type_defaults_to_unknown():
    result = process_events([
        {"event_id": 1, "timestamp": 100, "payload": {"x": 1}},
    ])

    assert result["validEvents"][0]["type"] == "unknown"

def test_full_pipeline_mixed():
    input_data = [
        {"event_id": 10, "type": "create", "timestamp": 200, "payload": {"id": 1}},
        {"event_id": 10, "type": "create", "timestamp": 100, "payload": {"id": 1}},
        {"event_id": 12, "timestamp": 150, "payload": {"id": 2}},
        {"event_id": 13, "type": "update", "timestamp": 180},
    ]

    result = process_events(input_data)

    assert len(result["validEvents"]) == 2
    assert len(result["invalidEvents"]) == 1

    assert result["validEvents"][0]["event_id"] == 10
    assert result["validEvents"][0]["timestamp"] == 100
    assert result["validEvents"][1]["event_id"] == 12
    assert result["validEvents"][1]["type"] == "unknown"

    assert result["invalidEvents"][0]["event_id"] == 13

def test_all_invalid():
    input_data = [
        {"event_id": 1, "timestamp": 100},
        {"event_id": 2, "timestamp": 200},
        {"event_id": 3, "timestamp": 300},
    ]

    result = process_events(input_data)

    assert len(result["validEvents"]) == 0
    assert len(result["invalidEvents"]) == 3)
