import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
    with connection.cursor() as cursor:
        sql = "insert into emp values(12, 'python', 1011, 1)"
        cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted...!!!!")


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
    with connection.cursor() as cursor:
        sql = "insert into emp values(%s, %s, %s, %s)"
        data = (13, 'klm', 1100, 1)
        cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted...!!!!")


def testInsert3(id, name, salary, deptId):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
    with connection.cursor() as cursor:
        sql = "insert into emp values(%s, %s, %s, %s)"
        data = (id, name, salary, deptId)
        cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted...!!!!")


def testInsert4(data):
    id = data["id"]
    name = data["name"]
    salary = data["salary"]
    deptId = data["deptId"]

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
    with connection.cursor() as cursor:
        sql = "insert into emp values(%s, %s, %s, %s)"
        data = (id, name, salary, deptId)
        cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted...!!!!")


# testInsert1()
# testInsert2()
# testInsert3(14, 'aaa', 1200, 2)

params = {}
params["id"] = 16
params["name"] = "kkk"
params["salary"] = 1500
params["deptId"] = 1
testInsert4(params)
