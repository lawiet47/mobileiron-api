from mobileiron_api.api.device_management_api import DeviceManagementAPI
from typing import Optional, Tuple


class MobileIronCloudAPI(object):
    device_management_api: DeviceManagementAPI

    def __init__(self, username: str, password: str, fqdn: str, timeout: Tuple[int, int]=(10, 60)):
        self._username = username
        self._password = password
        self._fqdn = fqdn
        self.device_management_api = DeviceManagementAPI(username=username, password=password, fqdn=fqdn,
                                                         timeout=timeout)
