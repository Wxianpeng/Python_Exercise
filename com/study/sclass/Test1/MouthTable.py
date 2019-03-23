class MultiplicationTable:
    def __init__(self, num):
        self.num = num

    def printTable(self):
        for i in range(2, self.num + 1):
            for x in range(2, i + 1):
                print('%d X %d = %d' % (i, x, i * x), end='\t')
            print('  ')


multiple = MultiplicationTable(10)

multiple.printTable()


