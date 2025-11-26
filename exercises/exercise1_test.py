
import pytest
from exercise1 import transform_workday_to_salesforce

def test_valid_transformation():
    input_data = {
        "id": 100,
        "email": "john@example.com",
        "department": "Sales",
        "start_date": "2025-01-15",
        "phone": None
    }

    result = transform_workday_to_salesforce(input_data)

    assert result["success"] is True
    assert result["data"]["employeeId"] == 100
    assert result["data"]["contact"]["phoneNumber"] == "N/A"
    assert result["data"]["metadata"]["group"] == "Sales"
    assert result["data"]["metadata"]["startDate"] == "1/15/2025"

def test_department_trim():
    input_data = {
        "id": 1,
        "email": "a@b.com",
        "department": "  Engineering  ",
        "start_date": "2024-02-01"
    }
    result = transform_workday_to_salesforce(input_data)
    assert result["data"]["metadata"]["group"] == "Engineering"

def test_phone_kept_if_provided():
    input_data = {
        "id": 1,
        "email": "a@b.com",
        "department": "IT",
        "start_date": "2024-01-01",
        "phone": "123-456"
    }
    result = transform_workday_to_salesforce(input_data)
    assert result["data"]["contact"]["phoneNumber"] == "123-456"

@pytest.mark.parametrize("missing_key", ["id", "email", "department", "start_date"])
def test_missing_required_fields(missing_key):
    input_data = {
        "id": 1,
        "email": "a@b.com",
        "department": "IT",
        "start_date": "2024-01-01"
    }
    del input_data[missing_key]

    result = transform_workday_to_salesforce(input_data)
    assert result["success"] is False
    assert result["error"] == "Missing required fields"
    assert "input" in result

def test_invalid_date():
    result = transform_workday_to_salesforce({
        "id": 1,
        "email": "a@b.com",
        "department": "Sales",
        "start_date": "bad-date"
    })
    assert result["success"] is False
    assert result["error"] == "Invalid date"

def test_invalid_date_empty_string():
    result = transform_workday_to_salesforce({
        "id": 1,
        "email": "a@b.com",
        "department": "Sales",
        "start_date": ""
    })
    assert result["success"] is False
    assert result["error"] == "Invalid date"

def test_returns_input_on_failure():
    bad_input = {"x": 1}
    result = transform_workday_to_salesforce(bad_input)
    assert result["success"] is False
    assert result["input"] == bad_input
