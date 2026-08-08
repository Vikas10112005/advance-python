import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "update student set name = 'pranav' where id =11"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = ('amit', 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')


def testUpdate3(name, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated3 successfully')


def testInsert4(data):
    id = data['id']
    name = data['Name']
    rollno = data['rollno']
    age = data['age']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()

    # Correction 1: Added '=' after age (age= %s)
    sql = "update student set name= %s, rollno= %s, age= %s where id = %s"

    # Correction 2: Order of variables should match the placeholders in the SQL query
    tuple_data = (name, rollno, age, id)

    cursor.execute(sql, tuple_data)
    connection.commit()
    connection.close()

    # Correction 3: Changed message to 'updated' since it is an UPDATE query
    print('data updated successfully')


#testUpdate1()
#testUpdate2()
#testUpdate3('ankit', 3)


params={}
params['id'] = 1
params['Name'] = 'vikas'
params['rollno'] = '110'
params['age'] = 21

testInsert4(params)