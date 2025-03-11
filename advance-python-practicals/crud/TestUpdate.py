import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
cursor = connection.cursor()
sql = "update marksheet set name = 'nidhi' where id = 2"
cursor.execute(sql)
connection.commit()
connection.close()
print('data updated successfully')
