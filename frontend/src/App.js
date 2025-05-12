import React, { useState, useEffect } from 'react';
import MovieList from './components/MovieList';
import MovieForm from './components/MovieForm';
import MovieRecommendation from './components/MovieRecommendation';

function App() {
  const [movies, setMovies] = useState([]);
  const [userRatings, setUserRatings] = useState([]);
  const [recommendedMovies, setRecommendedMovies] = useState([]);

  // Fetch list of movies from the backend
  useEffect(() => {
    fetch('http://localhost:8000/movies')  // Make sure the port matches the Flask backend
      .then(res => res.json())
      .then(data => setMovies(data));
  }, []);

  const handleRating = (movieId, rating) => {
    const userId = 1;  // Example user ID (this could be dynamic or logged-in user)
    fetch('http://localhost:8000/rate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ movie_id: movieId, user_id: userId, rating }),
    }).then(() => {
      setUserRatings([...userRatings, { movieId, rating }]);
    });
  };

  const handleRecommendation = () => {
    fetch('http://localhost:8000/recommendations?user_id=1&num_recommendations=5')  // Adjust the API call to backend
      .then(res => res.json())
      .then(data => setRecommendedMovies(data));
  };

  return (
    <div>
      <h1>Movie Recommender</h1>
      <MovieList movies={movies} onRate={handleRating} />
      <button onClick={handleRecommendation}>Get Recommendations</button>
      <MovieRecommendation movies={recommendedMovies} />
    </div>
  );
}

export default App;
