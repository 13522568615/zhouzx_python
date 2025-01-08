from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")
time.sleep(5)
# 找到搜索框
search_box = driver.find_element(By.NAME, "wd")

# 输入搜索关键词
search_box.send_keys("Selenium Python")

# 提交搜索
search_box.send_keys(Keys.RETURN)

# 等待页面加载
time.sleep(2)

# 获取搜索结果的标题
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
print("")
for index, result in enumerate(results):
    print(f"结果 {index + 1}: {result.text}")

# 关闭浏览器
driver.quit()
