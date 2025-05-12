import React from 'react';

const MovieRecommendation = ({ movies }) => {
  return (
    <div>
      <h2>Recommended Movies</h2>
      <ul>
        {movies.map((movie, index) => (
          <li key={index}>{movie}</li>
        ))}
      </ul>
    </div>
  );
};

export default MovieRecommendation;
