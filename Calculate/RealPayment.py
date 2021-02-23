# -*- coding: utf-8 -*-
# @Time    : 2021/02/23 15:08:00
# @Author  : DannyDong
# @File    : RealPayment.py
# @Describe: Calc Real Payment Api

import random

from locust.user import TaskSet, task


class RealPayment(TaskSet):
    
    @task
    def calc_real_payment(self):
        """
        Desc: 计算实付款接口
        """
        url = '/calculate/calcMoney'
        # 构造测试数据
        goods_num = random.randint(1, 5)
        unit_price = [{"id": i + 1, 'goodsPrice': str(random.randint(5, 15))} for i in range(goods_num)]
        with self.client.post(url, json={"unitPrice": unit_price, "actualPrice":"50"}) as response:
            return response
