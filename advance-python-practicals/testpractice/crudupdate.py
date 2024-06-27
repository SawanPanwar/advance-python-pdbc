import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
cursor = connection.cursor()
sql = "update tablepdbc set name='Snehaa' where id=4"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data updated successfully")
