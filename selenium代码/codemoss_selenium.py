import time, os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CodeMoss(object):

    def __init__(self):
        self.url = "https://pc.aihao123.cn/index.html?#/chat"
        self.driver = webdriver.Chrome()

    def read_excel(self):
        path = os.path.dirname(os.path.dirname(__file__))
        data = os.path.join(path, 'selenium代码/codemoss_data.xlsx')
        df = pd.read_excel(data, index_col=None, header=None)
        test_data = []
        for row in df.itertuples(index=False):
            test_data.append({"name": row[0], "type": row[1], "element": row[2], "text": row[3], "times": row[4],
                              "procedure": row[5]})

        del test_data[0]
        return test_data

    def out_moss(self):
        time.sleep(10)
        self.driver.quit()

    def element_click_xpath(self, Xpath):
        self.driver.find_element(By.XPATH, str(Xpath)).click()

    def element_click_id(self, id):
        self.driver.find_element(By.ID, str(id)).click()

    def element_text_xpath(self, Xpath, text):
        self.driver.find_element(By.XPATH, str(Xpath)).send_keys(text)

    def element_text_id(self, id, text):
        self.driver.find_element(By.ID, str(id)).send_keys(text)

    def element_times(self, times):
        time.sleep(times)

    def login_moss(self):
        print(self.read_excel())
        self.driver.get(self.url)

        for data in self.read_excel():
            print(data['procedure'])
            if data['name'] == "click":
                if data['type'] == "xpath":
                    self.element_click_xpath(data['element'])
                if data['type'] == "id":
                    self.element_click_id(data['element'])
            if data['name'] == "text":
                if data['type'] == "xpath":
                    self.element_text_xpath(data['element'], data['text'])
                if data['type'] == "id":
                    self.element_text_id(data['element'], data['text'])
            if data['name'] == "times":
                self.element_times(data['times'])

        self.out_moss()


if __name__ == '__main__':
    CodeMoss().login_moss()
