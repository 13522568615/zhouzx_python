import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化 WebDriver
        cls.driver = webdriver.Chrome()  # 或者使用其他浏览器的 WebDriver
        cls.driver.implicitly_wait(10)  # 设置隐式等待时间

    def test_search_python(self):
        # 打开 Google
        self.driver.get("https://www.baidu.com")

        # 查找搜索框并输入搜索内容
        search_box = self.driver.find_element(By.NAME, "wd")
        search_box.send_keys("Python")
        search_box.send_keys(Keys.RETURN)  # 模拟按下回车键

        # 等待搜索结果加载
        time.sleep(2)

        # 验证搜索结果页面标题
        self.assertIn("Python", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        # 关闭 WebDriver
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
