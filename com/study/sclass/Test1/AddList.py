# 请直接运行并体验代码

class 出租车():
    def __init__(self, 参数1, 参数2, 参数3):
        self.每公里费用 = 参数1
        self.最低公里 = 参数2
        self.最低费用 = 参数3

    def 计费(self):
        self.记录行程()
        self.统计费用()
        self.结算信息()

    def 记录行程(self):
        self.行程公里数 = float(input('请输入行程公里数：'))

    def 统计费用(self):
        if self.行程公里数 <= self.最低公里:
            self.最终费用 = self.最低费用
        else:
            self.最终费用 = self.最低费用 + (self.行程公里数 - self.最低公里) * self.每公里费用

    def 结算信息(self):
        print('费用一共是：' + str(self.最终费用) + '元')




class 电动车(出租车):

    def 统计费用(self):
        if self.行程公里数 <= self.最低公里:
            self.最终费用 = self.最低费用 * 0.8
        else:
            self.最终费用 = (self.最低费用 + (self.行程公里数 - self.最低公里) * self.每公里费用) * 0.8


小王的出租车 = 出租车(2.5, 3, 15)

小王的出租车.计费()

小李的电动车 = 电动车(2.5, 3, 15)

小李的电动车.计费()
