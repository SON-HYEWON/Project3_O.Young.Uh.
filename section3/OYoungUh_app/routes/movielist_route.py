from flask import Blueprint, render_template, request, session
from OYoungUh_app.models.movielist_model import Movie
from OYoungUh_app.models.user_model import User
from OYoungUh_app.models.points_models import Points
from OYoungUh_app import db

bp = Blueprint('movielist', __name__)

@bp.route('/')
def index():
    """
    영화 목록 페이지
    """
    movies = Movie.query.all()

    if 'user_id' not in session:
        return render_template('movielist.html', movies=movies)

    # 로그인 되어 있다면, 해당 유저의 평점을 불러옴
    one_user_id = session.get('user_id', None)
    points = Points.query.filter(Points.user_id == one_user_id).all()
    
    points_dict = {}
    
    for a in points:
        points_dict[a.title] = a.point
    
    return render_template('movielist.html', movies=movies, points_dict=points_dict)


@bp.route('/search', methods=['POST'])
def search():
    """
    영화 검색 기능
    """
    if request.method == 'POST':
        input_value = dict(request.form)
        value = input_value['input_value']

        if input_value['mybrowser_movie'] == 'title':
            if 'user_id' not in session: # 로그인이 없으면 search만 해 줌
                movies = Movie.query.filter(Movie.title.like(f'%{value}')).all()
            # 로그인 되어 있다면, 해당 유저의 평점을 불러옴
            one_user_id = session.get('user_id', None)
            points = Points.query.filter(Points.user_id == one_user_id).all()
            points_dict = {}
            
            for a in points:
                points_dict[a.title] = a.point
            
            movies = Movie.query.filter(Movie.title.like(f'%{value}')).all()
            return render_template('movielist.html', movies=movies, points_dict=points_dict)

        elif input_value['mybrowser_movie'] == 'genre':
            if 'user_id' not in session: # 로그인이 없으면 search만 해 줌
                movies = Movie.query.filter(Movie.genre.like(f'%{value}')).all()
            # 로그인 되어 있다면, 해당 유저의 평점을 불러옴
            one_user_id = session.get('user_id', None)
            points = Points.query.filter(Points.user_id == one_user_id).all()
            points_dict = {}
            
            for a in points:
                points_dict[a.title] = a.point
            
            movies = Movie.query.filter(Movie.genre.like(f'%{value}')).all()
            return render_template('movielist.html', movies=movies, points_dict=points_dict)


@bp.route('/', methods=['POST'])
def re_points():
    """
    영화 평점 기록
    """
    if request.method == 'POST':

        # 로그인이 없으면 로그인을 요구하는 문구 요구
        if 'user_id' not in session: 
            return render_template('index.html', alert_need_login=True)

        # 로그인 되어 있다면, 해당 유저의 평점을 불러와서 수정
        else: 
            one_user_id = session.get('user_id', None)
            input_name = list(request.form)[1]
            input_points = dict(request.form)['points'] ######## points 인지 체크!!!!

            points_db = Points.query.filter(Points.user_id == one_user_id, Points.title == input_name).first()

            if not points_db: # 평점을 기록한 적이 없다면, 새로운 평점 추가
                new_point = Points(user_id=one_user_id, title=input_name, point=input_points)
                db.session.add(new_point)
            else: # 이전 평점기록이 있다면, 이를 수정
                points_db.point = input_points

        db.session.commit()

        movies = Movie.query.all()
        points = Points.query.filter(Points.user_id == one_user_id).all()
    
        points_dict = {}
    
        for a in points:
            points_dict[a.title] = a.point
    
        return render_template('movielist.html', movies=movies, points_dict=points_dict)