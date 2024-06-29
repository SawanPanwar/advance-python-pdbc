import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python')
try:
    connection.autocommit(False)
    cursor = connection.cursor()
    sql = "insert into user values(6,'Shalini','Tiwari','106Shalini','abc','2003,5,21','Indore')"
    sql2 = "insert into user values(7,'Shalini','Tiwari','107Shalini','abc','2003,5,21','Indore')"
    sql3 = "insert into user values(7,'Shalini','Tiwari','107Shalini','abc','2003,5,21','Indore')"
    cursor.execute(sql)
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.close()
    print('data inserted successfully')
except Exception as e:
    connection.rollback()
    print('exception: ', e)
