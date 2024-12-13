# tests/test_create_resource.py
import pytest
from api_framework.request_builder import RequestBuilder
from api_framework.utils import load_json_file, get_base_url


def test_create_resource():
    base_url = get_base_url()
    endpoint = load_json_file("endpoints/create_endpoint.json")["create"]
    data = load_json_file("test_data/create_data.json")

    response = (RequestBuilder()
                .set_url(f"{base_url}{endpoint}")
                .set_method("POST")
                .add_header("Content-Type", "application/json")
                .set_data(data)
                .build())

    assert response.status_code == 201
    pytest.created_id = response.json()["id"]
