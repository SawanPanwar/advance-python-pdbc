import pymysql


class studentModel:
    def newPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "select max(id) from tablepdbc"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[0] is not None:
            pk = result[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = self.newPk()
        emp_id = data['emp_id']
        name = data['name']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "insert into tablepdbc (id, emp_id, name, salary) values (%s, %s, %s, %s)"
        data = (id, emp_id, name, salary)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('Data inserted successfully')

    def update(self, data):
        id = data['id']
        emp_id = data['emp_id']
        name = data['name']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "update tablepdbc set emp_id=%s, name=%s, salary=%s where id=%s"  # Corrected SQL syntax
        data = (emp_id, name, salary, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('Data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "delete from tablepdbc where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('Data deleted successfully')

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "select * from tablepdbc"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        connection.close()

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "select * from tablepdbc where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        connection.commit()
        connection.close()

    def findbyempId(self, empId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "select * from tablepdbc where emp_id = %s"
        data = (empId)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        connection.commit()
        connection.close()

    def search(self, data):
        name = data.get('name', '')
        empId = data.get('empId', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='practicepdbc')
        cursor = connection.cursor()
        sql = "select * from tablepdbc where 1=1"
        if name != '':
            sql += " and name='" + name + "'"
        if empId != 0:
            sql += " and empId= " + str(empId)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        connection.commit()
        connection.close()
