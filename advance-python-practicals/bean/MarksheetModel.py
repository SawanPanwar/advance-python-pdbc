import pymysql
import MarksheetBean
from MarksheetBean import *


class MarksheetModel:
    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select max(id) from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for d in result:
            if d[0] is not None:
                pk = d[0]
        return pk + 1

    def add(self, bean):
        pk = MarksheetModel.nextPk(self)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
            data = (pk, bean.getName(), bean.getRollNo(), bean.getPhysics(), bean.getChemistry(), bean.getMaths())
            cursor.execute(sql, args=data)
        connection.commit()
        connection.close()
        print("Data Inserted...!!!!")

    def update(self, bean):
        pk = MarksheetModel.nextPk(self)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "update marksheet set  name = (%s), roll_no = (%s), physics = (%s), chemistry = (%s), maths = (%s) where id = (%s)"
            data = (
                bean.getName(), bean.getRollNo(), bean.getPhysics(), bean.getChemistry(), bean.getMaths(), bean.getId())
            cursor.execute(sql, args=data)
        connection.commit()
        connection.close()
        print("Data Update...!!!!")

    def delete(self, id):
        pk = MarksheetModel.nextPk(self)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "delete from marksheet where id = (%s)"
            data = (id)
            cursor.execute(sql, args=data)
        connection.commit()
        connection.close()
        print("Data Deleted...!!!!")

    def search(self):
        result = ''
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select * from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def findById(self, id):
        result = ''
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='adv_python_test')
        with connection.cursor() as cursor:
            sql = "select * from marksheet where id = (%s)"
            data = (id)
            cursor.execute(sql, args=data)
            result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
