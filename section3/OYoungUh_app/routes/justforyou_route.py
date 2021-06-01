from flask import Blueprint, render_template, request, session
from OYoungUh_app.utils.login_funcs import sign_in, match_id
bp = Blueprint('justforyou', __name__)

@bp.route('/')
def index():
    return render_template('justforyou.html')