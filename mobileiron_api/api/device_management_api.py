from mobileiron_api.api.base_api import BaseAPI
from .constants import MOBILE_IRON_SPACE_ID
import urllib

from typing import List, Optional, Tuple


class DeviceManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, timeout: Tuple[int, int]):
        super(DeviceManagementAPI, self).__init__(username, password, fqdn, "device", timeout)

    def get_device_from_email(self,
                              email: str,
                              ) -> Optional[dict]:

        filters = {
            'emailAddress': email,
            'dmPartitionId': MOBILE_IRON_SPACE_ID
        }

        efilter = "&".join(["{0}={1}".format(str(x), str(y)) for x, y in filters.items()])
        print(efilter)
        params = {'fq': efilter}
        response = self._call(params=params)

        return response.json()
