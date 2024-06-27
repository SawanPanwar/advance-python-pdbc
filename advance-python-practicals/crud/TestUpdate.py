import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
cursor = connection.cursor()
sql = "update marksheet set name = 'abc' where id = 1"
cursor.execute(sql)
connection.commit()
connection.close()
print('data updated successfully')
