# -*- coding: utf-8 -*-
# @Time    : 2021/02/22 15:05:08
# @Author  : DannyDong
# @File    : DemoTest.py
# @Describe: Locust Demo

from locust import HttpUser

from Format.JsonStr import FormatJson
from Calculate.RealPayment import RealPayment
from SecretCode.EncryptData import EncryptData
from SecretCode.DecryptData import DecryptData
from ToolHubHome.ToolHubHome import ToolHubHome
from FakerData.GenerateData import GenerateData


class RunLocust(HttpUser):
    # 注册压测任务
    tasks = [ToolHubHome, GenerateData, EncryptData, DecryptData, RealPayment, FormatJson]
    # 最小思考时间
    min_wait = 3000
    # 最大思考时间
    max_wait = 6000


if __name__ == "__main__":
    import os
    os.system("locust -f RunLocust.py --web-port=8098 --host=https://apitoolhub.mintblue.top/api/v1")
