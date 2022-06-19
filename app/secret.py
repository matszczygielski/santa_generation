import requests

from app.config import ONETIMESECRET_APIKEY, ONETIMESECRET_USERNAME


class Secret:
    def __init__(self, msg: str, ttl_s: int = 3600) -> None:
        self._url = None
        self._ttl = ttl_s
        self._msg = msg


    def generate(self) -> bool:
        auth = (ONETIMESECRET_USERNAME, ONETIMESECRET_APIKEY)
        data = f"secret={self._msg}&ttl={self._ttl}"

        response = requests.post("https://onetimesecret.com/api/v1/share", data=data, auth=auth)

        if not response.ok:
            return False

        r_json = response.json()
        self._url = f"https://onetimesecret.com/secret/{r_json['secret_key']}"
        return True


    @property
    def url(self):
        return self._url    
