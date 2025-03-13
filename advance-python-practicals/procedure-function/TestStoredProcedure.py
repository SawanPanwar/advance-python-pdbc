import pymysql


def empIn():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    cursor.callproc('empIn', [2])
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()


def empOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    cursor.execute('CALL empOut(@output)')
    cursor.execute("SELECT @output")
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()


def empInOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    cursor.execute('SET @input_output = 1')
    cursor.execute('CALL empInOut(@input_output)')
    cursor.execute("SELECT @input_output")
    result = cursor.fetchone()
    print(result[0])
    connection.close()


empIn()
# empOut()
# empInOut()
