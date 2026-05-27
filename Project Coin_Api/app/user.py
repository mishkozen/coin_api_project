class User:
    def __init__(self, name, password, address,  portfolio):
        self._name = name
        self._password = password
        self._address = address
        self._portfolio = portfolio

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def get_address(self):
        return self._address

    def get_portfolio(self):
        return self._portfolio

    def set_portfolio(self,portfolio):
        self._portfolio = portfolio