from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # 用户之间的等待时间，1到5秒之间


# 启动命令 locust -f locust代码/locustfile.py --host=http://www.baidu.com