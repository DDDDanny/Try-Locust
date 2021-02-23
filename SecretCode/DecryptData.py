# -*- coding: utf-8 -*-
# @Time    : 2021/02/23 14:46:17
# @Author  : DannyDong
# @File    : DecryptData.py
# @Describe: Decrypt Data API

from locust.user import TaskSet, task


class DecryptData(TaskSet):
    
    @task
    def decrypt_data(self):
        """
        Desc: 数据解密接口
        """
        url = '/secretCode/goDecrypt'
        with self.client.post(url, json={"cate":"1","waitStr":"SGVsbG9Xb3JsZAo="}) as response:
            return response
