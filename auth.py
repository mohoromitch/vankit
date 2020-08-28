import keyring


class Auth:
    @staticmethod
    def getCredential(app, username):
        return keyring.get_credential(app, username)

    @staticmethod
    def getPassword(app, username):
        return keyring.get_password(app, username)

    @staticmethod
    def setPassword(app, username, password):
        keyring.set_password(app, username, password)
