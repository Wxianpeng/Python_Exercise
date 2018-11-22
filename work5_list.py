# 列表定义

names = ["张三", "李四", "王五", "赵六", "李琪"]

# 列表支持 任何数据类型
nums = [100, 3.14, "100", "张三"]
print(nums)

print(names)

# 添加到原有的列表的最后
names.append("王八")
print(names)

# 位置 ， 要添加的内容
names.insert(0, "八戒")
print(names)

# 按照位置添加
names.insert(2, "沙僧")
print(names)
names2 = ["大洼", "二娃", "三娃"]
# 列表合并
name3 = names + names2
# ==>  names.extend(names2)

# print(name3)
names.extend(names2)
print(names)

# 删除
# 删除最后一个  names.pop()(弹栈)  栈:后进先出   堆:先进先出
names.pop()
print(names)
# 根据内容删除
names.remove("八戒")
print(names)

# 按照下标删除
del names[0]

# 改

names[1] = "沙和尚"
print(names)

# 查   切片
# print(names[2:5])

# 存在与不存在
print("王五" in names)
print("李四" not in names)


