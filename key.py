import keyring
def db_user():
    keyring.set_password("db", "user", "admin123@side-projects")
    db_user = keyring.get_password("db", "user")
    return db_user


def db_password():
    keyring.set_password("db", "password", "Awan123!")
    db_password = keyring.get_password("db", "password")
    return db_password
