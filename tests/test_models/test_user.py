#!/usr/bin/env python3
import unittest
from backend.api.v1.models import User


class TestUsers(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.usr = User("octocat")

    @unittest.skip("limited request atm")
    def test_create_user(self):
        usr = User("Ostoyae")
        self.assertIsInstance(usr, User)

    @unittest.skip("limited request atm")
    def test_get_user_repo(self):
        self.usr.async_get_repos()
        self.assertNotEqual(self.usr.__repos, {})

    # @unittest.skip("limited request atm")
    def test_user_metrics(self):
        self.assertNotEqual(self.usr.lang_metric, {})

    @unittest.skip("auth not implementedt atm")
    def test_login_user(self):
        usr = User()
        self.assertTrue(usr.is_login)

    def test_not_login_user(self):
        self.assertFalse(self.usr.is_login)
