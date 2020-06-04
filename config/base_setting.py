# 设置服务器端口
SERVER_PORT = 8999
# 连接到数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/hmsx?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# cookie
AUTH_COOKIE_NAME = '1903_hmsx'

# 拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]
#开始
STATUS = {
    "1":"正常",
    "0":"已删除"
}