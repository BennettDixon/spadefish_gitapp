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
    "/me",
    methods=["GET"],
    strict_slashes=False
)
def get_me():
    usr = User()
    # usr.lang_metric()
    usr.lang_metric
    return jsonify(usr.to_dict())

@app_views.route(
    "/users/<name>",
    methods=["GET"],
    strict_slashes=False
)
def get_user(name=None):
    usr = User(name)
    usr.lang_metric
    return jsonify(usr.to_dict())