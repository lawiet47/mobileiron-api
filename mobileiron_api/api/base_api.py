import collections
from typing import Optional, Tuple
from base64 import b64encode

import requests


class BaseAPI:
    def __init__(self, username: str, password: str, fqdn: str, endpoint: str, dmPartitionId: int, timeout: Tuple[int, int]):
        self._username = username
        self._password = password
        self._fqdn = fqdn
        self._endpoint = endpoint
        self._requests_timeout = timeout
        self._dmPartitionId = dmPartitionId

    # build basic auth manually since auth parameter in requests is not accepted by MobileIron Cloud API
    def _build_headers(self) -> dict:
        auth_str = b64encode(bytes(f"{self._username}:{self._password}", "utf-8")).decode("ascii")
        return {
            "Authorization": "Basic {}".format(
                auth_str
            )
        }

    def _get_url(self, call_name: Optional[str] = None, endpoint: Optional[str] = None) -> str:
        endpoint = endpoint if endpoint is not None else self._endpoint
        return f"https://{self._fqdn}/api/v1/{endpoint}" if call_name is None else f"https://{self._fqdn}/api/v1/{endpoint}/{call_name}"

    def _call(self,
              call_name: Optional[str] = None,
              http_method: str = "get",
              params: str = None,
              json_value: object = None,
              header_params: dict = {},
              endpoint: Optional[str] = None) -> requests.Response:

        url = self._get_url(call_name=call_name, endpoint=endpoint)
        headers = self._build_headers()
        self.extend(headers, header_params)

        return self._execute_call(url=url,
                                  http_method=http_method,
                                  headers=headers,
                                  params=params,
                                  json_value=json_value)

    def _execute_call(self,
                      url: str,
                      http_method: str = None,
                      headers: dict = None,
                      params: str = None,
                      json_value: object = None):
        method = getattr(requests, http_method)
        if http_method == 'get' and params is not None:
            url = f"{url}?{params}"
        response = method(url, headers=headers, params=params if http_method != 'get' else None, json=json_value,
                          timeout=self._requests_timeout)
        response.raise_for_status()
        return response

    @staticmethod
    def extend(*args):
        if args is not None:
            result = None
            if type(args[0]) is collections.OrderedDict:
                result = collections.OrderedDict()
            else:
                result = {}
            for arg in args:
                result.update(arg)
            return result
        return {}
