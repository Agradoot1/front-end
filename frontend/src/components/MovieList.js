import React from 'react';

const MovieList = ({ movies, onRate }) => {
  return (
    <div>
      <h2>Available Movies</h2>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            {movie.title}
            <button onClick={() => onRate(movie.id, 5)}>Rate 5</button>
            <button onClick={() => onRate(movie.id, 3)}>Rate 3</button>
            <button onClick={() => onRate(movie.id, 1)}>Rate 1</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieList;
