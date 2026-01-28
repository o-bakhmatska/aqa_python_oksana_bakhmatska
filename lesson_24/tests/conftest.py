import pytest
import requests
from requests.auth import HTTPBasicAuth

from .config import AUTH_ENDPOINT, USERNAME, PASSWORD
from .logger import LOGGER


@pytest.fixture(scope="class")
def authed_session():
    session = requests.Session()

    LOGGER.info("Authenticating via %s ...", AUTH_ENDPOINT)
    resp = session.post(AUTH_ENDPOINT, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=10)

    assert resp.status_code == 200, f"Auth failed: {resp.status_code}, body={resp.text}"
    data = resp.json()
    assert "access_token" in data, f"No access_token in auth response: {data}"

    token = data["access_token"]
    session.headers.update({"Authorization": "Bearer " + token})

    LOGGER.info("Authentication OK. Token stored in session headers.")
    yield session

    session.close()
