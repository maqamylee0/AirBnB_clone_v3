#!/usr/bin/python3
"""view for city"""

from flask import jsonify, abort, request
from models import storage, City,  State
from api.v1.views import app_views


def init_cities(app_views):
    @app_views.route('/<state_id>/cities', methods=['GET'], strict_slashes=False)
    def get_cities_by_states(state_id):
        state = storage.get(State, state_id)
        if not state:
            abort(404)
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities)

    @app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
    def get_cities(city_id):
        city = storage.get(City, city_id)
        if not city:
            abort(404)
        return jsonify(city.to_dict())

    @app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
    def delete_cities(city_id):
        city = storage.get(City, city_id)
        if not city:
            abort(404)
        city.delete()
        storage.save()
        return jsonify({}), 200

    @app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
    def create_cities(state_id):
        state = storage.get(State, state_id)
        if not state:
            abort(404)

        if not request.is_json():
            abort(400, 'Not a JSON')

        data = request.get_json()

        if 'name' not in data:
            abort(400, 'Missing name')

        city = city(**data)
        city.state_id = state.id
        city.save()
        return jsonify(city.to_dict()), 201

    @app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
    def update_cities(city_id):
        city = storage.get(City, city_id)
        if not city:
            abort(404)

        if not request.is_json():
            abort(404, 'Not a JSON')

        data = request.get_json
        Ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in Ignore_keys:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
