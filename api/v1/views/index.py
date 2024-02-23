#!/usr/bin/python3
# routes 
from flask import jsonify

def init_app(app_views):
    @app_views.route('/status', methods=['GET'])
    def status():
        return jsonify({"status": "OK"})