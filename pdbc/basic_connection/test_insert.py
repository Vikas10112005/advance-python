import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
cursor = connection.cursor()
sql = "INSERT INTO STUDENT VALUES (2, 'Kabir', '1011', 20)"
cursor.execute(sql)
connection.commit()
print("Record inserted successfully")

