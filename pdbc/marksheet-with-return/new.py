import  pymysql

class marksheetmodle:

    def nextpk(self):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor = cursor.execute()
        result = cursor.fetchall()
        for data in result:
            if data[0] is None:
                pk = 0
            connection.commit()
            connection.close()
            return pk + 1

    def add(self,data):
        id = marksheetmodle.nextpk()
        name = data['name']
        rollno = data['rollno']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "insert into marksheet value (%s,%s,%s,%s,%s,%s)"
        data = ('id','name','rollno','physics','chemistry','maths')
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print()

    def update(self,data):
        id = data ['id']
        name = data['name']
        rollno = data['rollno']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
        cursor = connection.cursor()
        sql = "update marksheet set name =%s,rollno=%S,physics=%s,chemistry=%s,maths=%s"
        data = ('id','name','rollno','physics','chemistry','maths')
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print()

