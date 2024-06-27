import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(4, 104, 'pqr', 13, 48, 38)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (5, 105, 'pqr', 78, 67, 56)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert3(id, rollNo, name, physics, chemistry, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert4(data):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


# testInsert1()
# testInsert2()
# testInsert3(6, 106, 'pqr', 89, 77, 67)

params = {}
params['id'] = 7
params['rollNo'] = 107
params['name'] = 'klj'
params['physics'] = 70
params['chemistry'] = 67
params['maths'] = 79
testInsert4(params)
