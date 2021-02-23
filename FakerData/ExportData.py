# -*- coding: utf-8 -*-
# @Time    : 2021/02/23 11:29:51
# @Author  : DannyDong
# @File    : ExportData.py
# @Describe: Export Data API

import random

from locust.user import TaskSet, task


class ExportData(TaskSet):

    @task
    def export_data(self):
        """
        Desc: 导出随机数据
        """
        url = '/faker/export'
        dataNum = random.randint(1, 50)
        paramsList = '姓名,性别,电话,地址'
        with self.client.get(url, params={'paramsList': paramsList, 'dataNum': dataNum}) as response:
            return response
