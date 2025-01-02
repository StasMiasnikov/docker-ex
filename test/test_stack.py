import socket
from http import HTTPStatus
import pytest
import requests

AGENT_HOSTNAME = "localhost"
AGENT_PORT = ""
CONTROLLER_HOSTNAME = "localhost"
JOB_NAME = "curl-build"


def test_agent():
    try:
        with socket.create_connection((AGENT_HOSTNAME, 22)):
            assert False, "Agent is reachable"
    except (socket.timeout, ConnectionRefusedError, OSError):
        assert True, "Agent unreachable"


@pytest.mark.parametrize("host", [
    CONTROLLER_HOSTNAME,
])
def test_controller(host):
    try:
        response = requests.get(f"http://{host}:8080/")
        assert response.status_code == HTTPStatus.OK, f"Expected {HTTPStatus.OK} got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(e)


def test_job():
    try:
        response = requests.get(f"http://{CONTROLLER_HOSTNAME}:8080/job/{JOB_NAME}/api/json")
        assert response.status_code == HTTPStatus.OK, f"Expected {HTTPStatus.OK} got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"Failed to connect to Jenkins: {e}")
