from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class LoginCase(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.implicitly_wait(10)
		driver.maximize_window()
	print("设置完成")
	print("正在调用测试环境，请稍等....")

	def login(self,username,password):
		driver = self.driver
		driver.get("https://passport.cnblogs.com/user/signin")
		time.sleep(10)
		'''driver.find_element_by_id("userName").clear()'''
		driver.find_element_by_id("input1").send_keys(username)
		#driver.find_element_by_id("userPwd").clear()
		driver.find_element_by_id("input2").send_keys(password)
		driver.find_element_by_id("signin").click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[3]").click()

	def test_login_success(self):
		driver = self.driver
		self.login("縱橫傢、鬼谷","@long3692")
		print("正在进行测试，请稍等。。。。")
		time.sleep(15)
		try:
			link = driver.find_element_by_id('lnk_current_user')
			self.assertTrue("縱橫傢、鬼谷" in link.text)
			time.sleep(20)
			print("test_login_success pass,出现success已自动截图，在D:/success.png")
			self.driver.get_screenshot_as_file("D:/login_success.png")
		except:
			print("test_login_fail,出现fail文件已自动截图，在D:/error1.png")
			self.driver.get_screenshot_as_file("D:/login_fail.png")


	def test_login_fail(self):
		driver = self.driver
		self.login("縱橫傢、鬼谷","12323343")
		print("正在测试中，请稍等。。。。")
		time.sleep(20)
		error_message = driver.find_element_by_id("tip_btn").text
		self.assertIn('用户名或密码错误', error_message)
		driver.get_screenshot_as_file("D:/login_fail2.png")


	def teardown(self):
		driver = self.driver
		driver = quit()
		print("退出浏览器。。。")


if __name__ == '__main__':
	unittest.main()