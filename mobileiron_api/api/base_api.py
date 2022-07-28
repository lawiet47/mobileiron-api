import collections
from typing import Optional, Tuple
from base64 import b64encode

import requests


class BaseAPI:
    def __init__(self, username: str, password: str, fqdn: str, endpoint: str, timeout: Tuple[int, int]):
        self._username = username
        self._password = password
        self._fqdn = fqdn
        self._endpoint = endpoint
        self._requests_timeout = timeout

    # build basic auth
    def _build_headers(self) -> dict:
        auth_str = b64encode(bytes(f"{self._username}:{self._password}", "utf-8")).decode("ascii")
        return {
            "Authorization": "Basic {}".format(
                auth_str
            )
        }

    def _get_url(self, call_name: Optional[str]="") -> str:
        return f"https://{self._fqdn}/api/v1/{self._endpoint}"

    def _build_params(self, params_str: str):
        return f"{self._get_url()}?{params_str}"

    def _call(self,
              call_name: Optional[str] = "",
              http_method: str = "get",
              params: str = None,
              json_value: object = None,
              header_params: dict = {}) -> requests.Response:

        url = self._get_url(call_name=call_name)
        headers = self._build_headers()
        url = f"{url}?{params}"
        self.extend(headers, header_params)

        return self._execute_call(url=url,
                                  http_method=http_method,
                                  headers=headers,
                                  json_value=json_value)

    def _execute_call(self,
                      url: str,
                      http_method: str = None,
                      headers: dict = None,
                      json_value: object = None):
        response = None
        if http_method == 'get':
            response = requests.get(url, headers=headers, timeout=self._requests_timeout)
        elif http_method == 'post':
            response = requests.post(url, headers=headers, json=json_value, timeout=self._requests_timeout)
        elif http_method == 'put':
            response = requests.put(url, headers=headers, json=json_value, timeout=self._requests_timeout)
        elif http_method == 'delete':
            response = requests.delete(url, headers=headers, json=json_value, timeout=self._requests_timeout)
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
