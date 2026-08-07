import pymysql


def testread1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()

    print("data Read Successfully")


def testread2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    columnName = ('id', 'name', 'rollno', 'age')
    for x in data:
         print(x)
         print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()

    # sql = "select * from student"
    # sql = "select * from student where id = 1"
    # sql = "select * from student where rollno = '109'"
    # sql = "select * from student where name like 'a%'"
    sql = "select * from student where age = 23"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
    connection.close()


def testRead4(id, name, rollno , age):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()

    sql = 'select * from student'
    if id != 0:
        sql += " where id = " + str(id)
    if name != '':
        sql += " where name like '" + name + "%'"
    if rollno != '':
        sql += " where address like '" + rollno + "%'"
    if age != 0:
        sql += " where rollno = " + str(age)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])

    connection.commit()
    connection.close()

# testread1()
# testread2()
# testRead3()
testRead4(0, '', '', 109)