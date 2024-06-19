import pymysql


class MarksheetModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select max(id) from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            for d in result:
                if d[0] is not None:
                    pk = d[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = MarksheetModel.nextPk(self)
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

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select * from marksheet where id = %s"
            data = [id]
            cursor.execute(sql, data)
            result = cursor.fetchall()
            for data in result:
                print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def search(self, data):
        name = data.get("name", "")
        rollNo = data.get("rollNo", 0)
        pageNo = data.get("pageNo", 0)
        pageSize = data.get("pageSize", 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select * from marksheet where 1=1"
            if (name != ""):
                sql += " and name like '" + name + "%%'"
            if (rollNo != 0):
                sql += " and roll_no = " + str(rollNo)
            if (pageSize > 0):
                pageNo = (pageNo - 1) * pageSize
                sql += " limit %s, %s"
            print("sql => ", sql)
            cursor.execute(sql, [pageNo, pageSize])
            result = cursor.fetchall()
            for data in result:
                print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()
