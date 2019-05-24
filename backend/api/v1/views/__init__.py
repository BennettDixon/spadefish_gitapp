#!/usr/bin/python3
"""init file for views in REST API
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from backend.api.v1.views.user_view import *
# from backend api.v1.views.image_ocr import *
