import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
with connection.cursor() as cursor:
    cursor.execute("select * from marksheet")
    cursor.fetchall()
    meta = cursor.description
    for data in meta:
        print(data[0])
connection.close()
