#!/usr/bin/python3
""""view for place_review """
from flask import jsonify, abort, request
from models import storage, Place, Review, User
from api.vi.views import app_views

@app_views.route('/<place_id>/reviews', method=['GET'])
def get_list_of_reviews(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)

@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    review.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def creates_reviews(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    if not request.get_json:
        abort(404, 'Not a JSON')
    data = request.get_json

    if 'text' not in data:
        abort(404, 'Missing text')

    review = review(**data)
    review.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    
    if not request.get_json:
        abort(404, 'Not a JSON')
    
    data = request.get_json()
    Ignore_keys = ['id', 'user_id', 'place_id', 'created_at' 'updated_at']
    for key, value in data.items():
        if key not in  Ignore_keys:
            setattr(review, key, value)
    
    review.save()
    return jsonify(review.to_dict()), 200
    