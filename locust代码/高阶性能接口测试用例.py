# from locust import HttpUser, task, between
#
#
# class MyUser(HttpUser):  # 1、在类中继承locust.HttpUser的子类，也就是创建这个子类
#
#     # 添加locust给我们提供的函数between，里面1和2的值代表着每个task间隔1到2秒
#     wait_time = between(1, 2)
#
#     @task(1)  # 权重为1
#     def test_login_get(self):
#         resp = self.client.get('http://127.0.0.1:8080/login?username=admin&password=123')
#         print(resp.json())
#         assert resp.status_code == 200
#
#     @task(2)  # 权重为2，执行频率更高
#     def test_login_post(self):
#         resp = self.client.post("http://127.0.0.1:8080/login", data={"username": "admin", "password": "123"})
#         print(resp.json())
#         assert resp.status_code == 200


from locust import HttpUser, task, between, events

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_login_post(self):
        resp = self.client.post("http://127.0.0.1:8080/login", data={"username": "admin", "password": "123"})
        assert resp.status_code == 200
        # 设定响应时间不超过500ms
        if resp.elapsed.total_seconds() > 0.5:
            events.request_failure.fire(
                request_type="POST",
                name="test_login_post",
                response_time=resp.elapsed.total_seconds(),
                exception="Response time exceeded SLA"
            )