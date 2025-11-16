import pytest
from  lesson_14.homework14 import log_event

# from pathlib import Path
# BASE_PATH = Path(__file__).parent
#
# with open(BASE_PATH/'login_system.log') as f:
#     data = f.read()
#
# print(data)

LOG_FILE = "login_system.log"

def read_log():
    with open(LOG_FILE, "r") as f:
        return f.read()

@pytest.mark.parametrize("username,status",
                          [
                          ("Alice", "success"),
                          ("Ivan", "expired",),
                          ("Alice", "failed" ),
                          ]
                          )
def test_log_event_file(username, status):
    log_event(username, status)
    data = read_log()
    expected_message = f"Login event - Username: {username}, Status: {status}"
    assert expected_message in data


# Failed test will be expected as passed
def test_log_event_failed_message():
    username = "Alice1"
    status = "success"
    log_event(username, status)
    data = read_log()
    with pytest.raises(AssertionError):
        assert f"Login event - Username: WRONG_USER, Status: {status}" in data