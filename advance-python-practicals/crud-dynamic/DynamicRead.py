import pymysql


def testRead1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where name like 'a%'"
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead4(name):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where name like '" + name + "%'"
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead5(param={}):
    name = param.get('name', '')
    rollNo = param.get('rollNo', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where name like '" + name + "%'"
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead6(param={}):
    name = param.get('name', '')
    rollNo = param.get('rollNo', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    if name != '':
        sql += " where name = '" + name + "%'"
    if rollNo != 0:
        sql += " where roll_no = " + str(rollNo)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead7(param={}):
    name = param.get('name', '')
    rollNo = param.get('rollNo', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if name != '':
        sql += " and name = '" + name + "%'"
    if rollNo != 0:
        sql += " and roll_no = " + str(rollNo)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


# testRead1()
# testRead2()
# testRead3()
# testRead4("x")

param = {}
param['name'] = 'a'
param['rollNo'] = 101

# testRead5(param)

# testRead6(param)

testRead7(param)
