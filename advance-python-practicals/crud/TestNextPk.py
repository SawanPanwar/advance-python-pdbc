import pymysql

pk = 0
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
cursor = connection.cursor()
sql = "select max(id) from emp"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
for data in result:
    if data[0] is not None:
        pk = data[0]
connection.commit()
connection.close()

print(pk + 1)
