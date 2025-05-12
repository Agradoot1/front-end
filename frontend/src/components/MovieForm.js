import React, { useState } from 'react';
import axios from 'axios';

const MovieForm = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://localhost:5000/add_movie', { title, genre }).then(() => {
      onAdd();
      setTitle('');
      setGenre('');
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={title} onChange={e => setTitle(e.target.value)} placeholder="Title" required />
      <input value={genre} onChange={e => setGenre(e.target.value)} placeholder="Genre" required />
      <button type="submit">Add Movie</button>
    </form>
  );
};

export default MovieForm;
