import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
cursor = connection.cursor()
sql = "insert into marksheet values(3, 103, 'raj', 13, 48, 38)"
cursor.execute(sql)
connection.commit()
connection.close()
print('data inserted successfully')
