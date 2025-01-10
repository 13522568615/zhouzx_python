#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date  : 2023/12/25
# @Name  : ZhouZongXin

"""
重写ini源码，以及ini,yml读取封装
"""
import os
import configparser
import yaml

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
TEST_INI_PATH = os.path.join(PROJECT_PATH, "base_request_test.ini")  # 测试地址
DEV_INI_PATH = os.path.join(PROJECT_PATH, "base_request_dev.ini")  # 线上地址
HEADER_PATH = os.path.join(PROJECT_PATH, "base_herder.yaml")  # 存放header地址
TEMP_FILE = os.path.join(PROJECT_PATH, "temp_file.yaml")  # 临时文件
REPORT_PATH = os.path.join(PROJECT_PATH, "report/report.yaml")  # json测试报告存储位置


class MyConfigParser(configparser.ConfigParser):
    """
    重写源码optionxform方法，返回正常选项名
    """

    def __init__(self, defaults=None):
        super(MyConfigParser, self).__init__(defaults=None)

    def optionxform(self, optionstr):
        return optionstr


def load_ini(ini_path):
    """
    读取ini文件
    :param ini_path: ini文件地址
    :return:
    """
    conf_ini = MyConfigParser()
    conf_ini.read(ini_path)
    return conf_ini


def load_yaml(yaml_path):
    """
    读取yaml文件
    :param yaml_path: yaml文件地址
    :return:
    """
    with open(yaml_path, encoding="utf-8") as y:
        conf_yml = yaml.safe_load(y)
        if conf_yml is None:
            conf_yml = {}
            return conf_yml
    return conf_yml


def add_yaml(upData, yaml_path):
    """
    判断yaml文件是不是空，如果是空就添加新的数据到yaml文件内，如果不是空就保留原有数据并且添加新的到yaml文件内
    :param upData: 需要添加的数据
    :param yaml_path: yaml文件地址
    :return:
    """

    if os.path.getsize(yaml_path) == 0:
        content = {}
    else:
        with open(yaml_path, 'r') as file:
            content = yaml.safe_load(file)
            if content is None:
                content = {}

    content.update(upData)

    with open(yaml_path, 'w') as file:
        yaml.safe_dump(content, file)


def up_yaml(dict_data, yaml_path):
    """
    将传入新的字典后写到YAML文件中，此时会展示现有的字典
    :param dict_data: 传入字典
    :param yaml_path: yaml文件地址
    :return:
    """
    # 将传入新的字典后写到YAML文件中，此时会展示现有的字典
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(dict_data, file)


def del_yaml(yaml_path):
    """
    清空yaml文件内的所有数据
    :param yaml_path: yaml文件地址
    :return:
    """
    with open(yaml_path, 'w') as file:
        file.truncate(0)


if __name__ == '__main__':
    print(load_yaml(TEMP_FILE))
