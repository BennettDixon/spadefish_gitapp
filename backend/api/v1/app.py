#!/usr/bin/python3
"""main app file for Flask instance in REST API
"""
from flask import Flask, request, render_template, redirect, url_for
from flask import jsonify
from flask_dance.contrib.github import make_github_blueprint, github
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)
app.secret_key='justatest'

client_id = os.getenv('GITHUB_OAUTH_CLIENT_ID')
client_secret = os.getenv('GITHUB_OAUTH_CLIENT_SECRET')

blueprint = make_github_blueprint(client_id=client_id, client_secret=client_secret)

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    print('hi')
    if not github.authorized:
        print('notauthorized')
        return redirect(url_for("github.login"))
    git_obj=github.get("/user")
    print('this is the git_obj {}'.format(git_obj))
    assert git_obj.ok
    print(git_obj.json())
    return jsonify("{}".format(git_obj.json()))

@app.route('/authenticated')
def hello():
    print('this hello hi')
    git_obj=github.get("/user")
    print('this is the git_obj {}'.format(git_obj))
    assert git_obj.ok
    print(git_obj.json())
    return jsonify("{}".format(git_obj.json()))
    print(request.data)
    content = request.get_json()
    print(content)
    return content

def page_not_found(e):
    """404 error json response"""
    return jsonify({'error': "Not found"}), 404

@app.teardown_appcontext
def teardown_appcontext(exc=None):
    """called on teardown of app contexts of flask
    """
    pass


if __name__ == "__main__":
    """run the app if the script is not being imported
    """
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    fetched_host = os.environ.get('KIVY_API_HOST')
    fetched_port = os.environ.get('KIVY_API_PORT')
    if fetched_host is None:
        fetched_host = '0.0.0.0'
    if fetched_port is None:
        fetched_port = 5000
    app.run(host=fetched_host, port=fetched_port, threaded=True)
