# -*- coding: utf-8 -*-
# @Time    : 2021/02/23 15:37:41
# @Author  : DannyDong
# @File    : JsonStr.py
# @Describe: Format Json API

from locust.user import TaskSet, task


class FormatJson(TaskSet):
    
    @task
    def format_json(self):
        """
        Desc: 格式化Json字符串
        """
        url = '/format/json'
        request_body = {"jsonStr":"{\"data\":{\"result\":\"HelloWorld\"},\"meta\":{\"msg\":\"Success\",\"status\":200}}\n"}
        with self.client.post(url, json=request_body) as response:
            return response
