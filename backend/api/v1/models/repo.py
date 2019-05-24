# /usr/bin/env python3
"""
Define a class Repo
"""
from backend.api.v1.models import BaseModel
import requests_async as async_requests
import requests
import asyncio


# from api.v1 import portal


class Repo(BaseModel):
    name = ""
    owner = ""
    node_id = ""
    url = "http://github.com"
    __lang = {}
    is_owner = False
    is_forked = False

    def __init__(self, **kwargs):
        # kwargs["__lang"] = self.get_lang()
        super().__init__(**kwargs)

    @property
    def lang(self):
        return self.__lang

    def get_lang(self):
        resp = requests.get(
            f"https://api.github.com/repos/{self.owner}/{self.name}/languages"
        )
        return resp.json()


    def async_get_lang(self):
        """
        This method runs the Async version of get_lang
        :return: Dict of Key: <lang symbol> and Value <Number of Bytes>
        """
        resp = asyncio \
            .get_event_loop() \
            .run_until_complete(self.__aysnc_get_lang())
        self.__lang = resp.json()

    async def __aysnc_get_lang(self):
        """
        This Method builds the async future.
        :return: a future/promise
        """
        resp = await async_requests.get(
            f"https://api.github.com/repos/{self.owner}/{self.name}/languages"
        )
        return resp
