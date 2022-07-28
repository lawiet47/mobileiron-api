from mobileiron_api.api.base_api import BaseAPI
from .constants import MOBILE_IRON_SPACE_ID
import urllib

from typing import List, Optional, Tuple

from mobileiron_api.api.helpers.filters import request_search_filter


class DeviceManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, timeout: Tuple[int, int]):
        super(DeviceManagementAPI, self).__init__(username, password, fqdn, "device", timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_email(self,
                                   email: str,
                                   ) -> Optional[dict]:
        filters = {
            'emailAddress': email,
            'dmPartitionId': MOBILE_IRON_SPACE_ID
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return response.json()

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_id(self,
                                   id: int
                                   ) -> Optional[dict]:
        filters = {
            'deviceId': id,
            'dmPartitionId': MOBILE_IRON_SPACE_ID
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return response.json()
