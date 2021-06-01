from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)

    # db 연결
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SECRET_KEY'] = 'secretissecret'

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    # orm 연결    
    from OYoungUh_app.routes import (main_route, movielist_route, mypage_route, userrecommend_route, justforyou_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(movielist_route.bp, url_prefix='/movielist')
    app.register_blueprint(mypage_route.bp, url_prefix='/mypage')
    app.register_blueprint(userrecommend_route.bp, url_prefix='/userrecommend')
    app.register_blueprint(justforyou_route.bp, url_prefix='/justforyou')

    return app
