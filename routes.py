from flask import Blueprint, request, jsonify
from .recommender import recommend_movies
from .models import Movie, UserRating
from .database import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    movie_list = [{"id": movie.id, "title": movie.title} for movie in movies]
    return jsonify(movie_list) 

@main_bp.route('/rate', methods=['POST'])
def rate_movie():
    data = request.get_json()
    movie_id = data['movie_id']
    user_id = data['user_id']
    rating = data['rating']
    
    new_rating = UserRating(movie_id=movie_id, user_id=user_id, rating=rating)
    db.session.add(new_rating)
    db.session.commit()
    
    return jsonify({"message": "Rating saved successfully!"})

@main_bp.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id', type=int)
    num_recommendations = request.args.get('num_recommendations', default=5, type=int)
    
    recommended_movies = recommend_movies(user_id, num_recommendations)
    
    return jsonify(recommended_movies)
