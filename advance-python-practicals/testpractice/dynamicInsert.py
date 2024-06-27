import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
    cursor = connection.cursor()
    sql = "insert into tablepdbc values(5,105,'Harsh',35000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data inserted successfully")


# testInsert1()


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
    cursor = connection.cursor()
    sql = "insert into tablepdbc values(%s,%s,%s,%s)"
    data = (6, 106, 'Yash', 30000)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")


# testInsert2()


def testInsert3(id, emp_id, name, salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
    cursor = connection.cursor()
    sql = "insert into tablepdbc values(%s,%s,%s,%s)"
    data = (id, emp_id, name, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")


# testInsert3(7, 107, 'Tarun', 35000)


def testInsert4(data):
    id = data['id']
    emp_id = data['emp_id']
    name = data['name']
    salary = data['salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
    cursor = connection.cursor()
    sql = "insert into tablepdbc values(%s,%s,%s,%s)"
    data = (id, emp_id, name, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


x = {}
x['id'] = 8
x['emp_id'] = 108
x['name'] = 'Sumit'
x['salary'] = 25000
testInsert4(x)
