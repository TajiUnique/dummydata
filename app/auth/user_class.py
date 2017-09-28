# this script handles the operations to be performed on user accounts
# for example adding user or deleting user


class Userr(object):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password