from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(5, 15)  # 用户在任务之间等待的时间范围（秒）

    @task
    def visit_homepage(self):
        self.client.get("/")  # 访问首页

    @task
    def visit_product_page(self):
        self.client.get("/")  # 访问产品页面