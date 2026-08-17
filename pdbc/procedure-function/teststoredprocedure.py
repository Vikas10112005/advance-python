import pymysql


def studentIn():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()
    cursor.callproc('studentIn', [2])
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()


def studentOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()
    cursor.execute('CALL studentout(@output)')
    cursor.execute("SELECT @output")
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()


def studentInOut():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')
    cursor = connection.cursor()
    cursor.execute('SET @input_output = 1')
    cursor.execute('CALL studentInOut(@input_output)')
    cursor.execute("SELECT @input_output")
    result = cursor.fetchone()
    print(result[0])
    connection.close()


studentIn()
studentOut()
studentInOut()