import pymysql

# def testinsert():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
#     cursor = connection.cursor()
#     sql = "INSERT INTO Student VALUES (5, 'Mahi', '106', 20)"
#     cursor.execute(sql)
#     connection.commit()
#     connection.close()
#     print("Data Inserted Successfully")
#
#
#
# def testinsert2():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
#     cursor = connection.cursor()
#     sql = "INSERT INTO student VALUES (%s, %s, %s, %s)"
#     data=(6,'payal','108',21)
#     cursor.execute(sql,data)
#     connection.commit()
#     connection.close()
#     print("Data Inserted2 Successfully")
#
#
#
# def testInsert3(id, Name, age, rollNo):
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
#     cursor = connection.cursor()
#     sql = "insert into student values(%s, %s, %s, %s)"
#     data = (id, Name, rollNo, age)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('data inserted3 successfully')

def testInsert4(data):
    id = data['id']
    name = data['Name']
    rollNo = data['rollno']
    age = data['age']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()
    sql = "insert into student values(%s, %s, %s, %s)"
    data = (id, name, age, rollNo)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')



 #testinsert()
# testinsert2()
# testInsert3(6,'Harshit','109',23)
testInsert4({'id':'11',
             'Name':'Aman',
             'rollno':'110',
             'age':'23'})