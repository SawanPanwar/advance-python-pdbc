import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
with connection.cursor() as cursor:
    sql = "update emp set name = 'lak' where id = 10"
    cursor.execute(sql)
connection.commit()
connection.close()
print("Data Updated...!!!!")