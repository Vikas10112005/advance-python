import  pymysql


connection= pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
connection.autocommit(True)
cursor = connection.cursor()
sql1 = "insert into student values(3, 'DURGESH',114 , 21)"
sql2 = "insert into student values(4, 'amit', , 115,25)"
sql3 = "insert into student values(5, 'aman', , 116, 26)"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
connection.close()
print("data get successfully")