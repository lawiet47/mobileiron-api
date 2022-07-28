from mobileiron_api.client import MobileIronCloudAPI
import pytest


@pytest.fixture
def mobile_iron_client():
    return MobileIronCloudAPI("username", "password", "fqdn")
