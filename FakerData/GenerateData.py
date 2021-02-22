# -*- coding: utf-8 -*-
# @Time    : 2021/02/22 22:26:10
# @Author  : DannyDong
# @File    : GenerateData.py
# @Describe: Generate Data Api

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
