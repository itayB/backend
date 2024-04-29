from fastapi.testclient import TestClient
import pytest

from backend.__main__ import create_app

@pytest.fixture(scope="session")
def test_client():
    with TestClient(create_app()) as test_client:
        yield test_client
