list1 = ['A', 'B', 'C']

dict1 = {}

for i in range(3):
    order = int(input('你要把' + list1[i] + '放在第几位？（请输入数字1,2,3):'))
    dict1[order] = list1[i]

print(dict1)



list1 = [dict1[1], dict1[2], dict1[3]]

print(list1)

# 请你补全代码，实现：依次输入3，2，1，打印出排序后的列表['C','B','A']
