from flask import Blueprint, render_template, request
from OYoungUh_app.models.movielist_model import Movie
import random

bp = Blueprint('userrecommend', __name__)

@bp.route('/')
def index():
    """
    user에 따라 영화를 추천해 주는 페이지
    """
    movie_one = Movie.query.all()
    recomovie = random.choice(movie_one)

    return render_template('userrecommend.html', recomovie=recomovie), 200