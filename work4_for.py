# for 循环
# name = "admin"
# for temp in name:
#     print(temp)

Sn = 0
Sn20 = 0
# 打印1-100 的偶数
i = 1
while i <= 100:
    if i % 2 == 0:
        # print(i) 打印偶数
        if i <= 20:
            Sn20 += i
    Sn = Sn + i
    i += 1
print("1-100的偶数和 %d,1-20的偶数%d" % (Sn, Sn20))

# break continue

i = 1
while i < 10:
    i += 1
    print("------")
    if i == 5:
        #break
        continue
    print(i)

print("====")
