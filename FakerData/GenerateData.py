# -*- coding: utf-8 -*-
# @Time    : 2021/02/22 22:26:10
# @Author  : DannyDong
# @File    : GenerateData.py
# @Describe: Generate Data Api

import random

from locust.user import TaskSet, task


class GenerateData(TaskSet):

    @task
    def get_base_list(self):
        """
        Desc: 生成随机数据-获取基础菜单
        """
        url = '/faker/list/base'
        with self.client.get(url) as response:
            # 这里可以做判断
            return response

    @task
    def faker_data(self):
        """
        Desc: 生成随机数据
        """
        url = '/faker/random'
        # 请求体内容参数化
        faker_data = [
            {"cat":"100","attr":{"lastName":"","firstName":""}},
            {"cat":"101","attr":{"country":"","province":"","city":"","district":"","street":"","building":"","postcode":""}},
            {"cat":"102","attr":{"prefix":""}},
            {"cat":"103","attr":{"year":"","month":"","day":"","hour":"","minute":"","seconds":""}}
        ]
        request_body = random.choice(faker_data)
        with self.client.post(url, json=request_body) as response:
            # 这里可以做判断
            return response
