class Cat:
    def __init__(self, init_name, init_age):
        self.name = init_name
        self.age = init_age
        # print("我的名字是:%s" % self.name)

    def eat(self):
        print("%s eat  Something" % self.name)

    def sleep(self):
        print("The %s  is Sleeping" % self.name)

    def drink(self):
        print("The %s  drink something" % self.name)

    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))


tom = Cat("汤姆", 30)

tom.drink()
tom.introduce()
print("*" * 100)

cat = Cat("虹猫", 10)
cat.sleep()
cat.introduce()
