from OYoungUh_app import db

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(9))

    movie_points = db.relationship('Points', backref='movie', cascade='all, delete')

    def __repr__(self):
        return f"Tweet ID:{self.id}, movie title:{self.title}"