class Transcript():
    def __init__(self):
        self.name = input('请输入学生姓名：')
        self.chinese = int(input('请输入语文成绩：'))

        self.math = int(input('请输入数学成绩：'))

    def printTranscripts(self):
        print(self.name + '的成绩单如下：')
        print('语文成绩：' + str(self.chinese))
        print('数学成绩：' + str(self.math))


transcript1 = Transcript()  # 实例化
transcript2 = Transcript()  # 实例化
transcript3 = Transcript()  # 实例化

transcript1.printTranscripts()
transcript2.printTranscripts()
transcript3.printTranscripts()
