import keyring


def getCredential(app, username):
    return keyring.get_credential(app, username)


def getPassword(app, username):
    return keyring.get_password(app, username)


def setPassword(app, username, password):
    keyring.set_password(app, username, password)
