from OYoungUh_app.models.user_model import User
from OYoungUh_app import db

def sign_in(input_form):
    input_id = input_form['user_id']
    input_password = input_form['user_password']

    # db에 유저 정보가 있는지 확인
    user_db = User.query.filter(User.user_id == input_id).first()
    if not user_db: # db에 유저 정보가 없는 경우
        return (False, False)
    
    if input_password == user_db.user_password:
        return (True, user_db.user_id)
    else: # 비밀번호 틀림
        return (False, False)

def match_id(input_form):
    input_id = input_form['user_id']
    user_db = User.query.filter(User.user_id == input_id).first()

    if user_db: # 아이디가 이미 존재하는 경우
        return False
    else: # 새 계정 생성
        new_user = User(
        user_id=input_form['user_id'],
        user_password=input_form['user_password'])

    db.session.add(new_user)
    db.session.commit()

    return True
    