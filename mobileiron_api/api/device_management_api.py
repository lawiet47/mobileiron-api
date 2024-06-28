from requests import Response

from mobileiron_api.api.base_api import BaseAPI
from datetime import datetime, timedelta

from typing import List, Optional, Tuple, Dict, Union

from mobileiron_api.api.helpers.helpers import convert_times


class DeviceManagementAPI(BaseAPI):
    def __init__(self, username: str, password: str, fqdn: str, endpoint: str, dmPartitionId: int,
                 timeout: Tuple[int, int]):
        super(DeviceManagementAPI, self).__init__(username, password, fqdn, endpoint, dmPartitionId, timeout)

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_email(self,
                                      email: str,
                                      ) -> Optional[Dict]:
        """
        :param email: email of the owner of the device
        :return: Dictionary of the results
        """
        params = 'fq=emailAddress={0}&dmPartitionId={1}'.format(email, self._dmPartitionId)
        response = self._call(endpoint='device', params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_id(self,
                                   id: int
                                   ) -> Optional[Dict]:
        """
        :param wifimac: device ID of the device to retrieve
        :return: Dictionary of the results
        """
        params = 'fq=deviceId={0}&dmPartitionId={1}'.format(id, self._dmPartitionId)
        response = self._call(endpoint='device', params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profile_from_mac(self,
                                    wifimac: str
                                    ) -> Optional[Dict]:
        """
        :param wifimac: wifiMac address of the device to retrieve
        :return: Dictionary of the results
        """
        params = 'fq=wifiMacAddress={0}&dmPartitionId={1}'.format(wifimac, self._dmPartitionId)
        response = self._call(endpoint='device', params=params)
        return convert_times(json_data=response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757067
    def get_device_profiles_bulk(self,
                                 rows: int = 100,
                                 start: int = 0,
                                 sort: bool = True) -> Optional[Dict]:
        """
        :param sort: Sorts the results by id
        :param rows: Integer to determine how many results will be returned in a call.
        :param start: Offset which the results will be shown off of.
        :return:  Dictionary of results
        """
        params = "rows={0}&start={1}&dmPartitionId={2}&sortFields%5B0%5D.name=id&sortFields%5B0%5D.order=ASC".format(rows, start, self._dmPartitionId) if sort else ("rows={0}&start={1}&dmPartitionId={2}".format(rows, start, self._dmPartitionId))
        response = self._call(endpoint='device', params=params)
        return convert_times(response.json())

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757147
    def lock_devices(self,
                     ids: Union[str, List[str]],
                     pin: int,
                     display_message: str
                     ) -> Optional[Dict]:
        """
        Locks a given number of devices.
        :param ids: IDs of the target devices to lock
        :return: returns the result of the http request
        """
        if isinstance(ids, str):
            ids = [ids]

        ids = "&".join(["ids={0}".format(id) for id in ids])
        params = "{0}&message={1}&phoneNumber=osxLockPin={2}".format(ids, display_message, pin)
        response = self._call(endpoint='device', call_name="lock", http_method="put", params=params)
        return response.json()

    # https://help.ivanti.com/mi/help/en_us/cld/76/api/Content/MobileIronCloudCustomerIntegrationAPIGuide/Device%20API%20Calls.htm#_Toc507757147
    def unlock_devices(self,
                       ids: Union[str, List[str]]
                       ) -> Optional[Dict]:
        """
        Locks a given number of devices.
        :param ids: IDs of the target devices to lock
        :return: returns the result of the http request
        """
        if isinstance(ids, str):
            ids = [ids]

        ids = "&".join(["ids={0}".format(id) for id in ids])
        params = ids
        response = self._call(endpoint='device', call_name="unlock", http_method="put", params=params)
        return response.json()

    def retire_device(self,
                      ids: Union[str, List[str]]
                      ) -> Optional[Dict]:
        """
        Retires a given number of devices.
        :param ids: IDs of the target devices to retire
        :return: returns the result of the http request
        """
        if isinstance(ids, str):
            ids = [ids]

        ids = "&".join(["ids={0}".format(id) for id in ids])
        params = ids
        response = self._call(endpoint='device', call_name="retire", http_method="put", params=params)
        return response.json()

    def delete_device(self,
                      ids: Union[str, List[str]]
                      ) -> Optional[Dict]:
        """
        Deletes a given number of devices.
        :param ids: IDs of the target devices to delete
        :return: returns the result of the http request
        """
        if isinstance(ids, str):
            ids = [ids]

        ids = "&".join(["deviceIds={0}".format(id) for id in ids])
        params = ids
        response = self._call(endpoint='device', http_method="delete", params=params)
        return response.json()