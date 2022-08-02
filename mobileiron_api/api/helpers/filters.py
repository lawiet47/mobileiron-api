from enum import Enum
from typing import List, Any, Optional


def request_search_filter(key: Optional[str] = None, params: Optional[dict] = None) -> str:
    """
    Creates a filter.

    :param key: the dictionary key to hold the stringfied version of url parameters
    :param params: parameters that need to be passed in the url (decoded)
    :return: the filter
    """
    # Convert parameters because the API does not support urlencoded parameters
    filter = "&".join(["{0}={1}".format(str(x), str(y)) for x, y in params.items()])

    return f"{key}={filter}" if key is not None else f"{filter}"
