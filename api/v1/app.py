#!/usr/bin/python3
"""Status of API"""


from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views

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
    app.run(host="0.0.0.0", port="5000", threaded=True)
