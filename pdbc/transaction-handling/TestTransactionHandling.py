import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college')

try:
    connection.autocommit(False)
    cursor = connection.cursor()
    sql1 = "insert into student values(4, kabir, '115', 20, 48)"
    sql2 = "insert into student values(5, amit, '116', 21, 48)"
    sql3 = "insert into student values(6, pravanv, '117', 22)"

    cursor.execute(sql1)    
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.commit()
    print("Transaction committed successfully")
except Exception as e:
    connection.rollback()
    print("Transaction rolled back due to error:", e)