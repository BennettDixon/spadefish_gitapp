#/usr/bin/env python3
"""
Define a class Repo
"""
from models.BaseModel import BaseModel
# from api.v1 import portal
import requests

class Repo(BaseModel):
    r_name = ""
    owner = ""
    node_id = ""
    url = "http://github.com"
    _lang = {}
    is_owner = False
    is_forked = False

    def __init__(self, **kwargs):
        kwargs["lang"] = self.get_lang()
        super().__init__(kwargs)

    @property
    def lang(self):
        return self._langs

    def get_lang(self):
        self._lang = requests.get(
            f"https://api.github.com/repos/{self.owner}/{self.r_name}/languages"
        ).json()
        return self.get_lang()



