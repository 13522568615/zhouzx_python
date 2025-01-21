from flask import Flask, make_response

# Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # 这是路由,定义是GET请求还是POST请求方式，那么我们什么时候用到GET，什么时候用POST？规范是获取数据用GET，有参数请求或者修改数据用POST。看项目需要。
def run():  # 这是视图函数
    res = {
        'code': 0,
        'msg': "OK",
        'data': {
            'test': '测试页面'
        }
    }
    return make_response(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
