#!/usr/bin/env python3
import unittest
from backend.api.v1.models.user import User
from backend.api.v1.app import app
import requests



class TestUsers(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.usr = User("Ostoyae")

    @unittest.skip("limited request atm")
    def test_create_user(self):
        usr = User("Ostoyae")
        self.assertIsInstance(usr, User)

    @unittest.skip("limited request atm")
    def test_get_user_repo(self):
        self.usr.get_repos()
        self.assertNotEqual(self.usr.repo, {})

    @unittest.skip("limited request atm")
    def test_user_metrics(self):
        self.assertNotEqual(self.usr.lang_metric, {})

    @unittest.skip("auth not implementedt atm")
    def test_login_user(self):
        usr = User()
        self.assertTrue(usr.is_login)

    @unittest.skip("limited request atm")
    def test_not_login_user(self):
        self.assertFalse(self.usr.is_login)
