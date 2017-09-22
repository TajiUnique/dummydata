__author__ = 'joe'
# This test is used as a test case for user functionalities

import unittest

from app.auth.user_operation import UserManager


class FunctionalityTests(unittest.TestCase):
    def setUp(self):
        self.user = UserManager()

        # to assertain that email keyyed in is not an int value

        def test_login_email_for_int(self):
            self.assertRaises(ValueError, self.user.login(123, "abnoz"))

        def _test_login_email_for_int_if_pass_is_allInt(self):
            self.assertRaises(ValueError, self.user.login(175, 12344))

        def test_login_email_for_int_if_passwrd_is_mixed(self):
            self.assertRaises(ValueError, self.user.login, 123, "12344abnoz")
