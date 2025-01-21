#!/usr/local/bin python3.10
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: locust_api.py
# @Author: Mr.He
# @Time: 2月 17, 2023
# ---
from locust import HttpUser, task, between
import time
import requests as req
import json
import os
import random

import requests

headers = {}

time_list = []

def save_data(data):
    with open("./data.txtx", "a") as f:
        f.write(data)


def get_info():
    info = dict()
    f_num = random.randint(5000, 10000)
    desc = "你好，{}测试大数据推送速度{}".format(random.randint(1, 10000), f_num)
    l_desc = "哈哈哈，{}今天适合骑摩托{}".format(random.randint(1, 10000), f_num)
    time = random.randint(1600000000, 1630000000)
    c_time = "2023-02-16 18:{}:{}".format(random.randint(1, 29), random.randint(0, 60))
    u_time = "2023-02-16 18:{}:{}".format(random.randint(1, 29), random.randint(0, 60))
    info["f_num"] = f_num
    info["desc"] = desc
    info["l_desc"] = l_desc
    info["time"] = time
    info["c_time"] = c_time
    info["u_time"] = u_time
    return info


def data_format(info):
    data = {
        "id":125930,
        "xingtu_id":"202311317071",
        "share_id":"20231111",
        "short_id":"1317061",
        "dy_num":"zzy17061",
        "nick_name":"测试抖音入库17051",
        "sec_uid":"",
        "is_star":1,
        "is_live":1,
        "is_online":1,
        "is_superstar":0,
        "grade":2,
        "gender":1,
        "follower_num":info["f_num"], #
        "province":"河南",
        "city":"沧州",
        "avatar_url":"https:\/\/p3.douyinpic.com\/aweme\/1080x1080\/aweme-avatar\/tos-cn-avt-0015_d008636d629a5f5d8c5db65465e5ffee.jpeg?from=4010531038",
        "star_description":info["desc"], #
        "live_description":info["l_desc"],#
        "account_create_time":info["time"], #
        "star_personal_tags":"",
        "star_industry_tags":"工具类软件-其他工具类软件,游戏-角色扮演,游戏-休闲游戏",
        "star_content_tags":"颜值达人",
        "star_content_tags_level":"美女",
        "star_content_tags_relation":"{\"颜值达人\":[\"美女\"]}",
        "live_personal_tags":"",
        "live_industry_tags":"",
        "live_content_tags":"颜值达人",
        "live_content_tags_level":"美女",
        "live_content_tags_relation":"",
        "star_price_info_json":"[{\"xingtu_id\":\"6629726511920316420\",\"desc\":\"1-20s视频\",\"field\":\"price\",\"settlement_desc\":\"固定价格\",\"settlement_type\":2,\"task_category\":1,\"video_type\":1,\"enable\":1,\"is_open\":1,\"price\":2000,\"origin_price\":2000},{\"xingtu_id\":\"6629726511920316420\",\"desc\":\"21-60s视频\",\"field\":\"price\",\"settlement_desc\":\"固定价格\",\"settlement_type\":2,\"task_category\":1,\"video_type\":2,\"enable\":1,\"is_open\":1,\"price\":2300,\"origin_price\":2300}]",
        "live_price_info_json":"[]",
        "xingtu_mcn_name":"啊就是贱啊啊啥",
        "xingtu_mcn_logo":"https://p6-starfe-sign.xingtu.cn/tos-cn-i-9hvokabxw2/9b1086075c43498498857fb44979081e~tplv-9hvokabxw2-image.jpeg?x-expires=1966164675&x-signature=h77iA9kjoWORkVs8Z5J8mNd61%2B0%3D ",
        "xingtu_mcn_introduction":"阿斯利康多久啊啥的111",
        "create_time":info["c_time"], #
        "update_time":info["u_time"], #
        "sync_type":"douyin_xingtu_accounts_info"
    }
    return data


class QuickstartUser(HttpUser):
    # global time_list
    wait_time = between(0.2, 0.4)
    @task
    def function1(self):
        global time_list
        _data = data_format(get_info()) # 写参数
        with self.client.post(url='/api/source_sync/douyinSynchro', json=_data, headers=headers, verify=False, catch_response=True) as res:
            save_data(str(res.elapsed.total_seconds()) + ",")
            try:
                con = res.json()
                if con.get('code') == 200 and res.elapsed.total_seconds() <= 0.2:
                    res.success(f'nice:, {res.elapsed.total_seconds()}')
                elif con.get('code') == 200 and res.elapsed.total_seconds() > 0.2:
                    res.failure(f'Request Delay:, {res.elapsed.total_seconds()}')
                else:
                    res.failure(res.json())
            except:
                res.failure(f'请求失败: {res.json()}')


def test_api():
    # url = "http://202.101.32.156:9080/weiq/weibo/mediaList"
    url = "http://im.ims.weiq.com/weiq/weibo/mediaList"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJodHRwOi8vMjAyLjEwMS4zMi4xNTY6OTA4MC91c2VyL2xvZ2luIiwiaWF0IjoxNjc2NDUyNDEyLCJleHAiOjE2NzY1Mzg4MTIsIm5iZiI6MTY3NjQ1MjQxMiwianRpIjoiUTZDNTRjekxRWWVCNFBvdyIsInN1YiI6IjQ3MjIzIiwicHJ2IjoiZjZiNzE1NDlkYjhjMmM0MmI3NTgyN2FhNDRmMDJiN2VlNTI5ZDI0ZCIsImd1YXJkIjoiYXBpIiwidWlkIjo0NzIyMywicm9sZSI6IjEifQ.HgFut6BySl3NKPtvYkQMvdmCclUo-zHn9e4VMOhZlapyFBYsNpszmT5OjVv9NbP303-0rQomY7N5Whfzx0Tb-A"
    }
    data = {
        "accountUid": "2718604160",
        "channel": "weibo",
        "newOrderProcess": True,
        "userLabel": 5
    }
    res = req.post(url=url, headers=headers, json=data)
    print(res.headers.items())
    print(res.json())


def test_api_():
    url = "http://im.ims.weiq.com/api/source_sync/douyinSynchro"
    data = data_format(get_info())
    res = requests.post(url=url, data=data)
    print(res.cookies)

if __name__ == '__main__':
    # test_api_()
    # test_api()

    now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    os.system("locust -f locust_api.py --headless -u 5 -r 1 -t 5s --host=http://im.ims.weiq.com --loglevel=INFO 1>log.log --csv=../locustReport/run_csv --html=../locustReport/report-{}.html".format(now))
    # # pass
    # print(time_list)