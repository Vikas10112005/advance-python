import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='testdemo')
cursor = connection.cursor()
sql = "INSERT INTO STUDENT VALUES (2, 'Kabir', 'Indore', 101)"
cursor.execute(sql)
connection.commit()
print("Record inserted successfully")

