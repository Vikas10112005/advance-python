import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='testdemo')
cursor = connection.cursor()
sql = "UPDATE EMPLOYEE SET NAME = 'RAM' WHERE ID = 1"
cursor.execute(sql)
connection.commit()
print("Record UPDATE successfully")

