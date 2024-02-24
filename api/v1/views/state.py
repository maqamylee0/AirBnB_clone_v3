#!/usr/bin/python3
# routes for state

from flask import jsonify
from models import storage

def init_state(app_views):
    @app_views.route('/states', methods=['GET'])
    def get_states():
        states = storage.all("State")
        return jsonify([state.to_dict() for state in states.values()])
    
    @app_views.route('/states/<state_id>', methods=['GET'])
    def get_state(state_id):
        state = storage.get("State", state_id)
        if state is None:
            return jsonify({"error": "Not found"})
        return jsonify(state.to_dict())
    
    @app_views.route('/states/<state_id>', methods=['DELETE'])
    def delete_state(state_id):
        state = storage.get("State", state_id)
        if state is None:
            return jsonify({"error": "Not found"})
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    
    @app_views.route('/states/<state_id>', methods=['PUT'])
    def put_state(state_id):
        state = storage.get("State", state_id)
        if state is None:
            return jsonify({"error": "Not found"})
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Not a JSON"})
        for key, value in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(state, key, value)
        storage.save()
        return jsonify(state.to_dict()), 200