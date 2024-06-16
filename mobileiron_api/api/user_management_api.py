from mobileiron_api.api.base_api import BaseAPI
from typing import List, Optional, Tuple, Dict

from mobileiron_api.api.helpers.helpers import convert_times


class UserManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, dmPartitionId: int, timeout: Tuple[int, int]):
        super(UserManagementAPI, self).__init__(username, password, fqdn, "account", dmPartitionId, timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/User%20API%20Calls.htm#_Toc507756843 {Reference Broken, to see scroll down}
    def get_user_profile_from_email(self,
                                    email: str,
                                    ) -> Optional[Dict]:
        params = 'fq=UID={0}'.format(email)
        response = self._call(params=params)
        return convert_times(response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/User%20API%20Calls.htm?Highlight=UID%3D#_Toc507756843
    # Sorting results are not implemented : ->
    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/MobileIron%20Cloud%20API%20Basics.htm#_Toc507756799
    def get_user_profiles_bulk(self,
                               rows: int = 100,
                               start: int = 0,
                               sort: bool = True) -> Optional[Dict]:
        params = "rows={0}&start={1}&sortFields%5B0%5D.name=id&sortFields%5B0%5D.order=ASC" if sort else ("rows={"
                                                                                                          "0}&start={"
                                                                                                          "1}")
        params = params.format(rows, start)

        response = self._call(params=params)
        return convert_times(response.json())

    def delete_user_profile_from_id(self,
                                    user_id: int,
                                    ) -> Optional[Dict]:
        params = 'id={0}'.format(user_id)
        response = self._call(http_method="delete", params=params)
        return convert_times(response.json())