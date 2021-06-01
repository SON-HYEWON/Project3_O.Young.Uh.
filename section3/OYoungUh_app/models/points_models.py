from OYoungUh_app import db

class Points(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(128), db.ForeignKey('movie.title'), nullable=False)
    point = db.Column(db.Integer(), nullable=False)


    def __repr__(self):
        return f"Points point:{self.point}"