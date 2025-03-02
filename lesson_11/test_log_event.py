import logging
import pytest
import os


def log_event(username, status, log_file="test.log"):
    """Логує подію входу."""
    logger = logging.getLogger("login_logger")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    logger.info(f"Login event - Username: {username}, Status: {status}")

    logger.removeHandler(file_handler)
    file_handler.close()

@pytest.fixture
def log_file():
    """Фікстура для створення та очищення файлу логування."""
    log_file_name = "test.log"
    yield log_file_name
    if os.path.exists(log_file_name):
        os.remove(log_file_name)

def test_log_success(log_file):
    """Перевіряє логування успішного входу."""
    username = "Clara Osvin Osvald"
    status = "success"
    log_event(username, status)

    with open(log_file, "r") as f:
        log_content = f.read()

    expected_log = f"Login event - Username: {username}, Status: {status}"
    assert expected_log in log_content

