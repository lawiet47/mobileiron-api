from mobileiron_api.api.base_api import BaseAPI
from typing import List, Optional, Tuple

from mobileiron_api.api.helpers.filters import request_search_filter


class UserManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, timeout: Tuple[int, int]):
        super(UserManagementAPI, self).__init__(username, password, fqdn, "device", timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/User%20API%20Calls.htm#_Toc507756843 {Reference Broken, to see scroll down}
    def get_user_profile_from_email(self,
                                   email: str,
                                   ) -> Optional[dict]:
        filters = {
            'UID': email
        }
        params = request_search_filter('fq', filters)
        response = self._call(params=params)
        return response.json()
