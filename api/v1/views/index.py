#!/usr/bin/python3
# routes 

from flask import jsonify
from api.v1.views import app_views
from models import storage

def init_app(app_views):
    @app_views.route('/status', methods=['GET'])
    def status():
        return jsonify({"status": "OK"})
    
    @app_views.route('/stats', methods=['GET'])
    def stats():
        stats = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
        }
        return jsonify(stats)

