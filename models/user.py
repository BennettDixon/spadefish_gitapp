#!/usr/bin/env python
"""
Define class User
"""

from models.BaseModel import BaseModel
from models.repo import Repo
from api.v1 import portal
import requests


class User(BaseModel):
    g_id = 0
    g_login = ""
    g_url = "http://github.com"
    repos = {}
    __lang_metric = {}

    def __init__(self, user=None):
        """
        This instantiates an new object, if a user and not provided the logged
        in user is used.
        :param user: optional param for check another users metrics on github
        """
        if user:
            me = requests.get(
                f"https://api.github.com/users/{user}/repos"
            ).json()
        else:
            me = portal.get("/user").json()
        data = dict(
            id=me["id"],
            g_login=me["login"],
            g_url=me["url"],
            repos={},
            lang_metric={}
        )
        super().__init__(**data)

    def get_repos(self):
        """
        This Method gets the user's repos processes and convert them to Objects
        :return: dictionary of Repo objects
        """
        resp = self.portal.get("/user/repos").json()
        for repo in resp:
            data = dict(
                id=repo["id"],
                owner=self.g_login,
                name=repo["name"],
                url=repo['html_url'],
                lang={},
                is_owner=(
                    True if repo['owner']['login'] == self.g_login else False
                ),
                is_fork=repo['fork']
            )
        self.update(data['id'], Repo(**data).get_lang())

    @property
    def lang_metric(self):
        if not self.__lang_metric:
            if not self.repos:
                self.get_repos()
            self.sum_lang()

        return self.__lang_metric

    @lang_metric.setter
    def lang_metric(self, value):
        self.__lang_metric = value

    def sum_lang(self):
        """
        This method looks at the 'lang' attribute of all the Repos and sums the
        key value pairs.

        :return: Sum of all the key value.
        """
        for repo in self.repos.values():
            for k, v in repo.lang.items():
                if k in self.__lang_metric.keys():
                    self.__lang_metric[k] += v
                else:
                    self.__lang_metric[k] = v
        return self.__lang_metric

    @property
    def lang_metric(self):
        if not self.__lang_metric:
            if not self.repos:
                self.get_repos()
            self.sum_lang()

        return self.__lang_metric

