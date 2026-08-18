import pymysql



class MarksheetModel:

    def nextPK(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[0] is not None:
            pk = result[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = MarksheetModel.nextPK(self)
        rollNo = data['rollNo']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = cursor.execute(sql, (id, rollNo, name, physics, chemistry, maths))
        connection.commit()
        connection.close()
        print("data inserted successfully")

    def update(self, data):
        id = data['id']
        rollNo = data['rollNo']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "update marksheet set rollNo=%s, name=%s, physics=%s, chemistry=%s, maths=%s where id=%s"
        data = cursor.execute(sql, (rollNo, name, physics, chemistry, maths, id))
        connection.commit()
        connection.close()
        print("data updated successfully")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password ='root', database='python')
        cursor = connection.cursor()
        sql = "delete from marksheet where id=%s"
        data =(id)
        data = cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("data deleted successfully")

    def get(self, id ):
        connection=  pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor =connection.cursor()
        sql = "select * from marksheet where id=%s"
        data = (id)
        cursor.execute(sql,data)
        result = cursor.fetchall()
        for data in result:
           print(data[0],data[1],data[2],data[3],data[4],data[5])
        connection.commit()
        connection.close()
        print("data get successfully")

    def findByRoll(self, rollNo):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "select * from marksheet where rollno = %s"
        data = (rollNo)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def search(self, data):
        name = data.get('name', '')
        rollNo = data.get('rollNo', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1"
        if name != '':
            sql += " and name = '" + name + "'"
        if rollNo != 0:
            sql += " and roll_no = " + str(rollNo)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()