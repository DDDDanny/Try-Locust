# -*- coding: utf-8 -*-
# @Time    : 2021/02/23 13:58:30
# @Author  : DannyDong
# @File    : EncryptData.py
# @Describe: Encrypt Data Api

import random

from locust.user import TaskSet, task


class EncryptData(TaskSet):

    @task
    def encrypt_data(self):
        """
        Desc: 数据加密接口
        """
        url = '/secretCode/goEncrypt'
        cate = str(random.randint(1, 4))
        with self.client.post(url, json={"cate": cate, "salt": "HelloLocust", "waitStr": "HelloWorld"}) as response:
            # 这里可以写判断
            return response
