# 导入pymysql模块
import pymysql

# 连接database
connect = pymysql.connect(host="localhost", user="root", password="123456", database="python", charset="utf8")


# sql = "insert into productInformation(Info,Price,Deal,ProductName,Place) values(%s,%s,%s,%s,%s)"

# 查询操作
def queryData():
    cursor = connect.cursor()
    sql = "SELECT * FROM productInformation"
    res = cursor.execute(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")


def increaseData(data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()

    # SQL 插入语句
    # sql = """INSERT INTO productInformation(Info,Price, Deal, ProductName, Place)VALUES (Info, Price,Deal, ProductName, Place)"""

    sql = "INSERT INTO productInformation(INFO, PRICE, DEAL, PRODUCTNAME, PLACE) VALUES (%s, %s, %s, %s, %s )"
    try:
        # 执行sql语句
        cursor.execute(sql, data)
        # 提交到数据库执行
        connect.commit()
    except:
        # 如果发生错误则回滚
        connect.rollback()


queryData()

increaseData(['Mac', 'Mohan', 20, 'M', 2000])
# Info = 'wuli'
# Price = '123456789'
# Deal = '123456789'
# ProductName = '123456789'
# Place = '123456789'
# cursor.executemany(sql, [Info, Price, Deal, ProductName, Place])
# 涉及写操作要注意提交
connect.commit()
