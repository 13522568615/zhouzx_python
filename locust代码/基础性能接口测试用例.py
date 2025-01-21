import locust


class MyUser(locust.HttpUser):  # 1、在类中继承locust.HttpUser的子类，也就是创建这个子类

    # 添加locust给我们提供的函数between，里面1和2的值代表着每个task间隔1到2秒
    wait_time = locust.between(1, 2)

    @locust.task  # 2、添加一个装饰器，表明这是性能测试用例
    def test_request(self):
        resp = self.client.get(url="http://127.0.0.1:8080/")  # 3、使用self.client去发送请求
        print(resp.json())
        assert resp.status_code == 200
