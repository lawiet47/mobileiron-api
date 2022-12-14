from mobileiron_api.api.base_api import BaseAPI
from datetime import datetime, timedelta

from typing import List, Optional, Tuple, Dict

from mobileiron_api.api.helpers.filters import request_search_filter
from mobileiron_api.api.helpers.helpers import convert_times


class DeviceManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, dmPartitionId: int, timeout: Tuple[int, int]):
        super(DeviceManagementAPI, self).__init__(username, password, fqdn, "device", dmPartitionId, timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_email(self,
                                      email: str,
                                      ) -> Optional[Dict]:
        filters = {
            'emailAddress': email,
            'dmPartitionId': self._dmPartitionId
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_id(self,
                                   id: int
                                   ) -> Optional[Dict]:
        filters = {
            'deviceId': id,
            'dmPartitionId': self._dmPartitionId
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_mac(self,
                                    wifimac: str
                                    ) -> Optional[Dict]:
        filters = {
            'wifiMacAddress': wifimac,
            'dmPartitionId': self._dmPartitionId
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profiles_bulk(self,
                                rows: int = 100,
                                start: int = 0) -> Optional[Dict]:
        """
        Returns the results of an XQL Query.
        :param rows: Integer to determine how many results will be returned in a call.
        :param start: Offset which the results will be shown off of.
        :return:  Dictionary of results
        """
        filters = {
            'rows': rows,
            'start': start,
            'dmPartitionId': self._dmPartitionId
        }
        params = request_search_filter(params=filters)
        response = self._call(params=params)
        return convert_times(response.json())
