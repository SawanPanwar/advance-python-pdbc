import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
with connection.cursor() as cursor:
    sql = "delete from emp where id = 13"
    cursor.execute(sql)
connection.commit()
connection.close()
print("Data Deleted...!!!!")