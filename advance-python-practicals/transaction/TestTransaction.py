import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
connection.autocommit(False)
try:
    with connection.cursor() as cursor:
        sql = "insert into emp values((%s), (%s), (%s), (%s))"
        cursor.execute(sql, (26, 'a', 1500, 1))
        cursor.execute(sql, (27, 'b', 1500, 1))
        cursor.execute(sql, (27, 'c', 1500, 1))
        cursor.execute(sql, (28, 'd', 1500, 1))
    connection.commit()
    print("Data Inserted Successfully...!!!")
except:
    connection.rollback()
    print("Duplicate primary key")
finally:
    connection.close()
