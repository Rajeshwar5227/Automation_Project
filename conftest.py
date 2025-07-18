import logging
import pytest
import yaml
import json

def pytest_configure(config):
    logging.basicConfig(
        filename='logs/test.log',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logging.info("=== Test Session Start ===")

@pytest.fixture(scope="session")
def config_data():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture
def test_data():
    with open("data/test_data.json") as f:
        return json.load(f)

