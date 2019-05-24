#!/usr/bin/env python3
"""
Handles Getting User info.
"""
from api.v1.views import app_views
from api.v1.models.user import User
from api.v1.app import github
from flask import Flask, jsonify, request, abort
import json
import requests

@app_views.route(
    "/user",
    methods=["GET"],
    strict_slashes=False
)
def get_user():
    usr = User()
    usr.get_repos()
    return jsonify(usr.to_dict())