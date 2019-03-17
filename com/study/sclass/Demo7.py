from builtins import input


class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']

    @classmethod
    def 念诗函数(cls):
        for item in cls.一首诗:
            print(item)


念诗类.念诗函数()


class 幸运():
    @classmethod
    def 好运翻倍(cls):
        print('好的，我把它存了起来，然后翻了888倍还给你：' + str(cls.幸运数 * 888))
        # 或者这样写也可以：
        # print('好的，我把它存了起来，然后翻了888倍还给你：%d' % (cls.幸运数*888))


# 增加参数
幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))

幸运.好运翻倍()
