#!/usr/bin/python3
"""main app file for Flask instance in REST API
"""
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
client_id = os.getenv('GITHUB_OAUTH_CLIENT_ID')
client_secret = os.getenv('GITHUB_OAUTH_CLIENT_SECRET')


app = Flask(__name__)
app.secret_key = "supersekrit"  # Replace this with your own secret!
blueprint = make_github_blueprint(
    client_id=client_id,
    client_secret=client_secret,
)

app.register_blueprint(app_views)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def home_page():
    return redirect("http://spadefish.holberton.us")


@app.route("/login")
def index():
    print('am i authorized {}'.format(github.authorized))
    if not github.authorized:
        print(url_for("github.login"))
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    print(resp.json())
    #  assert resp.ok
    return jsonify(resp.json())


@app.route("/status")
def status():
    if not github.authorized:
        return jsonify({'status': False})
    return jsonify({'status': True})


def page_not_found(e):
    """404 error json response"""
    return jsonify({'error': "Not found"}), 404


@app.route("/logout")
def logout():
    del app.blueprints['github'].token
    return jsonify({'hi': 'bennett'})


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
        fetched_port = 5005
    app.run(host=fetched_host, port=fetched_port, threaded=True)
