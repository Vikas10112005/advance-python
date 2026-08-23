import pymysql

class marksheetmodle:

  def nextpk(self):
      pk = 0
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='python')
      cursor = connection.cursor()
      sql = "select max(id) from marksheet"
      cursor.execute(sql)
      result=cursor.fetchall()
      for data in result:
          if data[0] is not None:
             pk = data[0]
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
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='python')
      cursor = connection.cursor()
      sql = "insert into marksheet value(%s,%s,%s,%s,%s,%s)"
      data = ('id','name','rollno','physics','chemistry','maths')
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print("data add successfully")

  def update(self,data):
      id = data['id']
      name = data['name']
      rollno = data['rollno']
      physics = data['physics']
      chemistry = data['chemistry']
      maths = data['maths']
      connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
      cursor = connection.cursor()
      sql = "dpdate marksheet set name=%s,rollno=%s,physics=%s,chemistry=%s,maths=%s,where id = %s "
      data = ('name','rollno','physics','chemistry','maths')
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print("success")

  def delete(self,id):
      connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
      cursor = connection.cursor()
      sql = "delete from marksheet where id =%s"
      data = ('id')
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print("delete")

  def get(self,id):
      connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python')
      cursor = connection.cursor()
      sql = "select * from marksheet where id =%s"
      data = (id)
      cursor.execute(sql,data)
      result = cursor.fetchall()
      colomnname = ("id", "rollNo", "name", "physics", "chemistry", "maths")
      res = []
      for x in result:
          res.append({colomnname[i]:x [i] for i, _ in enumerate[x]})
          connection.commit()
          return res
