#!/usr/bin/python3
"""
Handles processing of images and sending
them to the Vision Azure API.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from api.v1.settings import vision_subscription_key
import json
import requests


@app_views.route(
    '/image_ocr',
    methods=['POST'],
    strict_slashes=False)
def process_image(debug=False):
    """Processes an image by:
        -> sending the file to Vision Azure api
        -> returns a dictionary containing the caption
        and confidence level associated with that image
        TODO implement
    """
    # get the json data
    json_data = response.json()
    if json_data is None or type(json_data) is not list:
        return jsonify({'error': 'Not a JSON'}), 402

    return jsonify(caption_response.to_dict())


@app_views.route('/testing', methods=['GET'], strict_slashes=False)
def testing_api():
    return '{"status": "OK" }'
