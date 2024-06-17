import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
with connection.cursor() as cursor:
    sql = "select * from emp"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        # print(data)
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
connection.commit()
connection.close()
print("Data Inserted...!!!!")
