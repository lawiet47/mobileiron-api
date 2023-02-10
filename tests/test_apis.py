

def test_get_device_profile_from_email(requests_mock, mobile_iron_client, get_device_profile_from_email):
    requests_mock.get(mobile_iron_client.device_management_api._get_url(), json=get_device_profile_from_email)
    assert get_device_profile_from_email == mobile_iron_client.device_management_api.get_device_profile_from_email("")

def test_get_device_profile_from_id(requests_mock, mobile_iron_client, get_device_profile_from_id):
    requests_mock.get(mobile_iron_client.device_management_api._get_url(), json=get_device_profile_from_id)
    assert get_device_profile_from_id == mobile_iron_client.device_management_api.get_device_profile_from_id(1)


def test_get_device_profile_from_mac(requests_mock, mobile_iron_client, get_device_profile_from_mac):
    requests_mock.get(mobile_iron_client.device_management_api._get_url(), json=get_device_profile_from_mac)
    assert get_device_profile_from_mac == mobile_iron_client.device_management_api.get_device_profile_from_mac("")


def test_get_user_profile_from_email(requests_mock, mobile_iron_client, get_user_profile_from_email):
    requests_mock.get(mobile_iron_client.user_management_api._get_url(), json=get_user_profile_from_email)
    assert get_user_profile_from_email == mobile_iron_client.user_management_api.get_user_profile_from_email("")


def test_get_user_profiles_bulk(requests_mock, mobile_iron_client, get_user_profiles_bulk):
    requests_mock.get(mobile_iron_client.user_management_api._get_url(), json=get_user_profiles_bulk)
    assert get_user_profiles_bulk == mobile_iron_client.user_management_api.get_user_profiles_bulk()


def test_get_device_profiles_bulk(requests_mock, mobile_iron_client, get_device_profiles_bulk):
    requests_mock.get(mobile_iron_client.device_management_api._get_url(), json=get_device_profiles_bulk)
    assert get_device_profiles_bulk == mobile_iron_client.device_management_api.get_device_profiles_bulk()

def test_lock_device(requests_mock, mobile_iron_client, lock_device):
    requests_mock.put(mobile_iron_client.device_management_api._get_url(call_name="lock"), json=lock_device)
    assert lock_device == mobile_iron_client.device_management_api.lock_devices([], 0, "")

def test_unlock_device(requests_mock, mobile_iron_client, lock_device):
    requests_mock.put(mobile_iron_client.device_management_api._get_url(call_name="unlock"), json=lock_device)
    assert lock_device == mobile_iron_client.device_management_api.unlock_devices([])
