# tests/test_update_resource.py
import pytest
from api_framework.request_builder import RequestBuilder
from api_framework.utils import load_json_file, get_base_url


def test_update_resource():
    base_url = get_base_url()
    endpoint = load_json_file("endpoints/update_endpoint.json")["update"]
    endpoint = endpoint.replace("{id}", str(pytest.created_id))
    data = load_json_file("test_data/update_data.json")

    response = (RequestBuilder()
                .set_url(f"{base_url}{endpoint}")
                .set_method("PUT")
                .add_header("Content-Type", "application/json")
                .set_data(data)
                .build())

    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
