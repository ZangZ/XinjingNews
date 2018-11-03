from flask import Flask
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定 session 保存的位置
from flask_session import Session
from config import config
from info.modules.index import index_blu

# 初始化数据库
#  在Flask很多扩展里面都可以先初始化扩展的对象，然后再去调用 init_app 方法去初始化
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])

    # 通过app初始化
    db.init_app(app)


    # 初始化redis 存储对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 开启当前项目CSRF 保护,制作服务器验证功能
    CSRFProtect(app)

    # 设置session保存指定位置
    Session(app)

    # 注册蓝图
    app.register_blueprint(index_blu)

    return app
