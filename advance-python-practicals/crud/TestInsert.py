import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
with connection.cursor() as cursor:
    sql = "insert into emp values(12, 'python', 1011, 1)"
    cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted...!!!!")