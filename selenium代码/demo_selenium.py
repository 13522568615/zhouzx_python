from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()


try:
    # 打开百度首页
    driver.get("https://www.baidu.com")

    # 确保页面加载完成
    time.sleep(2)

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
    print("搜索结果标题：")
    for index, result in enumerate(results):
        print(f"结果 {index + 1}: {result.text}")

    # 点击第一个搜索结果（如果存在）
    if results:
        results[0].click()
        time.sleep(10)  # 等待页面加载

        # 打印当前页面的标题
        print("当前页面标题:", driver.title)
    time.sleep(10)
finally:
    # 关闭浏览器
    driver.quit()


from selenium.webdriver.support.ui import Select
# 找到下拉列表元素
dropdown = driver.find_element_by_id('dropdown_id')  # 替换为下拉列表的实际ID
# 创建 Select 对象
select = Select(dropdown)
# 选择选项，可以通过索引、值或可见文本选择
select.select_by_index(1)  # 选择第二个选项（索引从0开始）
# select.select_by_value('option_value')  # 通过值选择
# select.select_by_visible_text('Option Text')  # 通过可见文本选择
