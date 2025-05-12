from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100))
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'<Movie {self.title}>'

class UserRating(db.Model):
    __tablename__ = 'user_ratings'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    movie = db.relationship('Movie', back_populates='ratings')

    def __repr__(self):
        return f'<UserRating {self.user_id} rated {self.movie.title} as {self.rating}>'

Movie.ratings = db.relationship('UserRating', backref='movie', lazy=True)
