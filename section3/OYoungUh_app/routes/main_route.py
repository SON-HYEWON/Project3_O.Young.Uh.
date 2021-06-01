from flask import Blueprint, render_template, request, session
from OYoungUh_app.utils.login_funcs import sign_in, match_id
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/signup',  methods=["GET", "POST"])
def signup():
    """
    회원가입 페이지
    """
    if request.method == "GET":
        return render_template('signup.html')

    if request.method == "POST":
        input_form = request.form

        if len(input_form) != 2: # 모든 정보가 입력되지 않은 경우
            return render_template('signup.html', alert_need_info=True)
        
        new_id = match_id(input_form)
        if not new_id: # 중복된 계정이 존재하는 경우
            return render_template('signup.html', alert_overlapID=True)
        if new_id :# 정상적으로 계정을 생성한 경우
            return render_template('index.html', alert_success_signup=True)


@bp.route('/signin', methods=["GET", "POST"])
def signin():
    """
    로그인 페이지
    """
    if request.method == "GET":
        return render_template('signin.html')
        
    if request.method == "POST":
        input_form = request.form
        result = sign_in(input_form)

        # 회원 정보가 일치하면 로그인, 아니면 실패 메시지 출력
        if result[0]:
            session['user_id'] = result[1]
            return render_template('index.html', alert_login_success=True)
        else:
            return render_template('signin.html', alert_mismatch=True)


@bp.route('/signout')
def signout():
    session.clear()
    return render_template('index.html', alert_signout=True)