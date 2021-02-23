# -*- coding: utf-8 -*-
# @Time    : 2021/02/22 21:51:33
# @Author  : DannyDong
# @File    : ToolHubHome.py
# @Describe: ToolHub Home Api

import json

from locust.user import TaskSet, task


class ToolHubHome(TaskSet):

    @task
    def get_tool_hub_menu(self):
        """
        Desc: 获取ToolHub菜单接口
        """
        url = '/menu'
        # name参数可以控制Web端名称显示
        with self.client.get(url, name='Home GetMenu API') as response:
            # 这里可以做判断
            # print(response.json())
            return response
