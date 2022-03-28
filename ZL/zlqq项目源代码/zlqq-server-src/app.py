from flask import Flask, request, send_from_directory, url_for, render_template
from flask_socketio import SocketIO, emit
from utils import restful
from flask_avatars import Avatars, Identicon
import os
from hashlib import md5

# pip install gunicorn==20.1.0 eventlet==0.30.2 is working for me. Try this maybe.

BASE_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['AVATARS_SAVE_PATH'] = os.path.join(BASE_DIR, "media", "avatars")

socketio = SocketIO(app, cors_allowed_origins="*")

avatars = Avatars(app)

online_users = []


@app.route('/media/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(app.config['AVATARS_SAVE_PATH'], filename)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def connect():
    print("ip: " + request.remote_addr)
    print("sid: " + request.sid)


@socketio.on("disconnect")
def disconnect():
    sid = request.sid
    for user in online_users:
        if user['sid'] == sid:
            online_users.remove(user)
            emit("friend offline", {"user": user}, broadcast=True)
            break


@socketio.on("login")
def login(data):
    username = data.get('username')
    if not username:
        return restful.params_error("请传入用户名！")
    for user in online_users:
        if user['username'] == username:
            return restful.params_error("此用户名已经存在！")

    filenames = Identicon().generate(md5(username.encode("utf-8")).hexdigest())
    avatar_name = filenames[2]
    avatar_url = url_for("get_avatar", filename=avatar_name)
    # avatar_url = "/media/avatars/" + avatar_name
    user = {
        "username": username,
        "ip": request.remote_addr,
        "avatar": avatar_url,
        "sid": request.sid
    }
    users = online_users.copy()
    online_users.append(user)
    emit("friend online", {"user": user}, broadcast=True)
    return restful.ok(data={"user": user, "online_users": users})


@socketio.on("send message")
def send_message(data):
    to = data.get('to')
    if not to:
        return restful.params_error("请传入对方sid！")
    for user in online_users:
        if user['sid'] == to:
            break
    else:
        return restful.params_error("此用户不存在或已下线！")

    message = data.get('message')
    if not message:
        return restful.params_error("请传入消息内容！")
    emit("receive message", {"message": message, "from": request.sid}, room=[to])
    return restful.ok()

# eventlet/gevent/uWsgi：WebSocket协议，有一个好处，只要客户端一断开连接，服务器就能立马收到disconnect事件
# Flask自带的服务器：长轮询，每隔大约5分钟的时间向客户端发送消息，来判断客户端是否断开连接

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
