import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
cursor = connection.cursor()
sql = "UPDATE student SET NAME = 'RAM' WHERE ID = 1"
cursor.execute(sql)
connection.commit()
print("Record UPDATE successfully")

