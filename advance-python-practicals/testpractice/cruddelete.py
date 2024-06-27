import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
cursor = connection.cursor()
sql = "delete from tablepdbc where id=5"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data deleted successfully")
