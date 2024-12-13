# tests/test_delete_resource.py
import pytest
from api_framework.request_builder import RequestBuilder
from api_framework.utils import load_json_file, get_base_url


def test_delete_resource():
    base_url = get_base_url()
    endpoint = load_json_file("endpoints/delete_endpoint.json")["delete"]
    endpoint = endpoint.replace("{id}", str(pytest.created_id))

    response = (RequestBuilder()
                .set_url(f"{base_url}{endpoint}")
                .set_method("DELETE")
                .add_header("Content-Type", "application/json")
                .build())

    assert response.status_code == 204
