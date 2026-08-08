import pymysql



def testDelete():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "delete from student where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data Delete Successfully")


def testdelete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "delete from student where id= %s"
    data=(3,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete2 Successfully")

def testdelete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database="college")
    cursor = connection.cursor()
    sql = "delete from student where id= %s"
    data=(id,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete3 Successfully")
#testDelete()
#testdelete2()
testdelete3(11)