import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='testdemo')
cursor = connection.cursor()
sql = "DELETE FROM STUDENT WHERE ID = 2"
cursor.execute(sql)
connection.commit()
print("Record DELETE successfully")

