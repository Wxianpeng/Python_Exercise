# extend  合并  ；  append 整体添加

a = ["aa", "bb", "cc"]

b = ["cc", "dd"]

# a.append(b)
# a.extend(b)
# print(a)

# a = a.append(b)
# print(a)   # Non

# 字典
# 1.len  长度

info = {"name": "张三", "age": "18"}

print("字典的大小%s" % (len(info)))  # 键值对 的个数

# 2.keys   获取key 的名称

print(info.keys())

# 3. values    获取 values的值   *对象生成器

print(info.values())
print()
for temp in info.keys():
    print("获取的keys:  " + temp)
print()
for temp in info.values():
    print("获取的values:" + temp)

print()

#  4.取值
# 方式1
for temp in info.items():
    print("key=%s,value=%s" % (temp[0], temp[1]))
# 方式2 拆包
for a, b in info.items():
    print("key=%s,value=%s" % (a, b))

