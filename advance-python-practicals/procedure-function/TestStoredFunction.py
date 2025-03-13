import pymysql


def testFunction():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    cursor.execute('select square(10)')
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()


testFunction()
