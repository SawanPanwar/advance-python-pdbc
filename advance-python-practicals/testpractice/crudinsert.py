import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
cursor = connection.cursor()
sql = "insert into tablepdbc values(5,105,'Yash',30000)"
cursor.execute(sql)
connection.commit()
connection.close()
print('Data inserted successfully')
