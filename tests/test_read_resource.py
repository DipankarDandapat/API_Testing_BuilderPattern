# tests/test_read_resource.py
import pytest
from api_framework.request_builder import RequestBuilder
from api_framework.utils import load_json_file, get_base_url


def test_read_resource():
    base_url = get_base_url()
    endpoint = load_json_file("endpoints/read_endpoint.json")["read"]
    endpoint = endpoint.replace("{id}", str(pytest.created_id))

    response = (RequestBuilder()
                .set_url(f"{base_url}{endpoint}")
                .set_method("GET")
                .add_header("Content-Type", "application/json")
                .build())

    assert response.status_code == 200
    assert response.json()["id"] == pytest.created_id
