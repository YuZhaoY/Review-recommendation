import os
import logging
import sys
sys.path.append("..")

from logging.handlers import RotatingFileHandler
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate

from flasky.app.Config import Config, log_dir
from flasky.app.api.utils.log import DayRotatingHandler
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask_jwt_extended import JWTManager  # 在顶部导入


db = SQLAlchemy()
jwt = JWTManager()  # 与db放在一起
cors = CORS()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

     # 注册插件
    register_plugins(app)

    # 注册蓝图
    register_blueprints(app)

    # 注册日志处理器
    register_logging(app)

    # 注册错误处理函数
    register_errors(app)

    app.logger.info('Flask Rest Api startup')
    return app

def register_logging(app):
    app.logger.name = 'flask_api'
    log_level = app.config.get("LOG_LEVEL", logging.INFO)
    cls_handler = logging.StreamHandler()
    log_file = os.path.join(log_dir, datetime.date.today().strftime("%Y-%m-%d.log"))
    file_handler = DayRotatingHandler(log_file, mode="a", encoding="utf-8")

    logging.basicConfig(level=log_level,
                        format="%(asctime)s %(name)s "
                               "%(filename)s[%(lineno)d] %(funcName)s() %(levelname)s: %(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S",
                        handlers=[cls_handler, file_handler])

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler(os.path.join(log_dir, 'flask_api.log'),maxBytes=1024 * 1024 * 50, backupCount=5, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(name)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))

            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)


def register_plugins(app):
    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  # 添加到register_plugins函数中


def register_blueprints(app):
    from flasky.app.api.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/')

    from flasky.app.api.register_annually import register_annually_bp
    app.register_blueprint(register_annually_bp, url_prefix='/')

    from flasky.app.api.critic import critic_bp
    app.register_blueprint(critic_bp, url_prefix='/')

    from flasky.app.api.nearby_search import nearby_search_bp
    app.register_blueprint(nearby_search_bp, url_prefix='/')

    from flasky.app.api.user_popular import user_popular_bp
    app.register_blueprint(user_popular_bp, url_prefix='/')

    from flasky.app.api.emotions import emotions_bp
    app.register_blueprint(emotions_bp, url_prefix='/')

    from flasky.app.api.fake import fake_bp
    app.register_blueprint(fake_bp, url_prefix='/')

    from flasky.app.api.categories_numbers import categories_number_bp
    app.register_blueprint(categories_number_bp, url_prefix='/')

    from flasky.app.api.best_category import best_category_bp
    app.register_blueprint(best_category_bp, url_prefix='/')

    from flasky.app.api.city_best_business import city_best_business_bp
    app.register_blueprint(city_best_business_bp, url_prefix='/')

    from flasky.app.api.most_business import most_business_bp
    app.register_blueprint(most_business_bp, url_prefix='/')

    from flasky.app.api.most_category import most_category_bp
    app.register_blueprint(most_category_bp, url_prefix='/')

    from flasky.app.api.most_fivestars import most_fivestars_bp
    app.register_blueprint(most_fivestars_bp, url_prefix='/')

    from flasky.app.api.most_negative_star import most_negative_star_bp
    app.register_blueprint(most_negative_star_bp, url_prefix='/')

    from flasky.app.api.recent_weekstars import recent_weekstars_bp
    app.register_blueprint(recent_weekstars_bp, url_prefix='/')

    from flasky.app.api.review_number import review_number_bp
    app.register_blueprint(review_number_bp, url_prefix='/')

    from flasky.app.api.word_count import word_count_bp
    app.register_blueprint(word_count_bp, url_prefix='/')

    from flasky.app.api.friend_recommend import friend_recommend_bp
    app.register_blueprint(friend_recommend_bp, url_prefix='/')

    from flasky.app.api.Business_Referrals import business_referrals_bp
    app.register_blueprint(business_referrals_bp, url_prefix='/')

    from flasky.app.api.user_number import user_number_bp
    app.register_blueprint(user_number_bp, url_prefix='/')

    from flasky.app.api.userrecs import userrecs_bp
    app.register_blueprint(userrecs_bp, url_prefix='/')
    # from app.author import author_bp
    # app.register_blueprint(author_bp,url_prefix='/api/author')
    #
    # from app.books import books_bp
    # app.register_blueprint(books_bp,url_prefix='/api/books')



def register_errors(app):

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)