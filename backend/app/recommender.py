import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .models import Movie, UserRating
from .database import db

def recommend_movies(user_id, num_recommendations=5):
    ratings = UserRating.query.all()
    if not ratings:
        return []

    df = pd.DataFrame(
        [(r.user_id, r.movie_id, r.rating) for r in ratings],
        columns=['user_id', 'movie_id', 'rating']
    )
    pivot = df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    if user_id not in pivot.index:
        return []

    user_vector = pivot.loc[[user_id]]
    similarity = cosine_similarity(user_vector, pivot)[0]
    scores = pd.Series(similarity, index=pivot.index)

    most_similar = scores.sort_values(ascending=False)[1:4]
    similar_users = pivot.loc[most_similar.index]
    mean_scores = similar_users.mean().sort_values(ascending=False)

    seen_movies = df[df.user_id == user_id]['movie_id'].tolist()
    recommendations = mean_scores[~mean_scores.index.isin(seen_movies)].head(num_recommendations).index.tolist()

    movie_titles = [Movie.query.get(mid).title for mid in recommendations if Movie.query.get(mid)]
    return movie_titles
