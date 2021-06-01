from OYoungUh_app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.String(64), nullable=False, unique=True)
    user_password = db.Column(db.String(64), nullable=False)

    user_points = db.relationship('Points', backref='user', cascade='all, delete')


    def __repr__(self):
        return f"User ID:{self.user_id}"