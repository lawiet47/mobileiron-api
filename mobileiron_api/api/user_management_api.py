from mobileiron_api.api.base_api import BaseAPI
from typing import List, Optional, Tuple

from mobileiron_api.api.helpers.filters import request_search_filter
from mobileiron_api.api.helpers.helpers import convert_times


class UserManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, dmPartitionId: int, timeout: Tuple[int, int]):
        super(UserManagementAPI, self).__init__(username, password, fqdn, "account", dmPartitionId, timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/User%20API%20Calls.htm#_Toc507756843 {Reference Broken, to see scroll down}
    def get_user_profile_from_email(self,
                                   email: str,
                                   ) -> Optional[dict]:
        filters = {
            'UID': email
        }
        params = request_search_filter(key='fq', params=filters)
        response = self._call(params=params)
        return convert_times(response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/User%20API%20Calls.htm?Highlight=UID%3D#_Toc507756843
    # Sorting results are not implemented : ->
    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/MobileIron%20Cloud%20API%20Basics.htm#_Toc507756799
    def get_user_profiles_bulk(self,
                              rows: int = 50,
                              start: int = 0) -> Optional[dict]:

        filters = {
            'rows': rows,
            'start': start
        }
        params = request_search_filter(params=filters)
        response = self._call(params=params)
        return convert_times(response.json())
