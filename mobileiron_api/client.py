from mobileiron_api.api.device_management_api import DeviceManagementAPI
from mobileiron_api.api.user_management_api import UserManagementAPI
from typing import Optional, Tuple


class MobileIronCloudAPI(object):
    device_management_api: DeviceManagementAPI
    user_management_api: UserManagementAPI

    def __init__(self, username: str, password: str, fqdn: str, dmPartitionId: int, timeout: Tuple[int, int] = (10, 60)):
        self._username = username
        self._password = password
        self._fqdn = fqdn
        self.device_management_api = DeviceManagementAPI(username=username, password=password, fqdn=fqdn, dmPartitionId=dmPartitionId,
                                                         timeout=timeout)
        self.user_management_api = UserManagementAPI(username=username, password=password, fqdn=fqdn, dmPartitionId=dmPartitionId,
                                                     timeout=timeout)
