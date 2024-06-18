import pymysql


class MarksheetModel:

    def add(self, data):
        id = data["id"]
        name = data["name"]
        rollNo = data["rollNo"]
        physics = data["physics"]
        chemistry = data["chemistry"]
        maths = data["maths"]

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
            data = (id, name, rollNo, physics, chemistry, maths)
            cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Inserted...!!!!")

    def update(self, data):
        id = data["id"]
        name = data["name"]
        rollNo = data["rollNo"]
        physics = data["physics"]
        chemistry = data["chemistry"]
        maths = data["maths"]

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "update marksheet set name = %s, roll_no = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
            data = (name, rollNo, physics, chemistry, maths, id)
            cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated...!!!!")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "delete from marksheet where id = %s"
            data = (id)
            cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Deleted...!!!!")

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select * from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()
