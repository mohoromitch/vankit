import keyring
from constants import AUTH_PREFIX


class Auth:

    def __init__(self, app):
        self.service_name = AUTH_PREFIX + app

    def getCredential(self, username):
        return keyring.get_credential(self.service_name, username)

    def getPassword(self, username):
        return keyring.get_password(self.service_name, username)

    def setPassword(self, username, password):
        keyring.set_password(self.service_name, username, password)
