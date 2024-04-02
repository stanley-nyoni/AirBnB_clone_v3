#!/usr/bin/python3
"""Status of API"""


from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Page not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
