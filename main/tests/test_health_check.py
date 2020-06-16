import logging
import pytest
from os import getenv
from bootUp import app
from starlette.testclient import TestClient

logging.basicConfig(filename='testslogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

health_check_url= getenv('HEALTH_CHECK_URL')

@pytest.fixture(scope="module", name="client")
def fixture_client():
    with TestClient(app) as test_client:
        yield test_client

def test_database(client):
    response = client.get("/health_check")
    assert response.status_code == 200
    print('Health Checked!')