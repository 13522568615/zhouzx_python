from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 尝试从GET请求中获取参数
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=int)

    # 如果GET请求中没有参数，则尝试从POST请求中获取参数
    if username is None or password is None:
        username = request.form.get('username', type=str)
        password = request.form.get('password', type=int)

    # 验证用户名和密码
    if username == 'admin' and password == 123:
        response_data = {
            'code': 0,
            'msg': "OK",
            'data': {
                'test': f"{request.method.lower()}请求测试页面"
            }
        }
    else:
        response_data = {
            'code': 999,
            'data': f"无效的用户名或密码: {username} {password}"
        }

    return make_response(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
