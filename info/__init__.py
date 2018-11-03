from flask import Flask
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定 session 保存的位置
from flask_session import Session
from config import config







app = Flask(__name__)
# 加载配置
app.config.from_object(config["development"])

# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis 存储对象
redis_store = StrictRedis(host=config["development"].REDIS_HOST, port=config["development"].REDIS_PORT)

# 开启当前项目CSRF 保护,制作服务器验证功能
CSRFProtect(app)

# 设置session保存指定位置
Session(app)


