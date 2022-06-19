from app.secret import Secret


class Santa:
    def __init__(self, name) -> None:
        self._name = name
        self._forbidden_santas = []
        self._drawn_santa = None
        self._is_owned = False
        self._secret_url = "-"


    @property
    def name(self) -> str:
        return self._name


    @property
    def forbidden_santas(self) -> list:
        return self._forbidden_santas


    @property
    def drawn_santa(self) -> str:
        return self._drawn_santa


    @drawn_santa.setter
    def drawn_santa(self, santa_name: str):
        self._drawn_santa = santa_name
        secret = Secret(santa_name)
        if not secret.generate():
            print("Error while generating secret for {}".format(self._name))
            return
        self._secret_url = secret.url


    @property
    def secret_url(self) -> str:
        return self._secret_url

    
    @property
    def is_owned(self) -> bool:
        return self._is_owned


    @is_owned.setter
    def is_owned(self, state: bool) -> None:
        self._is_owned = state


    def has_drawn_santa(self) -> bool:
        return self._drawn_santa is not None


    def add_forbidden_santa(self, santa_name: str) -> None:
        self._forbidden_santas.append(santa_name)
