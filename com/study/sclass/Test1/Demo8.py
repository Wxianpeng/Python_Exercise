from builtins import print


class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文成绩 = int(input('请输入语文成绩：'))
        cls.数学成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 打印成绩单(cls):
        print("%s的成绩如下" % (cls.学生姓名))
        print("语文成绩:%d" % (cls.语文成绩))
        print("数学成绩:%d" % (cls.数学成绩))

    @classmethod
    def 平均分(cls):
        cls.平均分 = (cls.数学成绩 + cls.语文成绩) / 2
        print("%s的平均分是:%s" % (cls.学生姓名, cls.平均分))

    @classmethod
    def 等级(cls):
        平均分 = cls.平均分
        if 平均分 >= 90:
            print(cls.学生姓名 + '的评级是：优')
        elif 80 <= 平均分 < 90:
            print(cls.学生姓名 + '的评级是：良')
        elif 60 <= 平均分 < 80:
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')


成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.平均分()

成绩单.等级()
