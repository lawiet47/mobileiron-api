class MobileIronCloudAPI(object):
    def __init__(self, username: str, password: str, fqdn: str):
        self._username = username
        self._password = password
        self._fqdn = fqdn

