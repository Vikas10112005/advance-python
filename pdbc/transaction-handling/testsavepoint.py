import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='college',
                             autocommit=False)

cursor = connection.cursor()

try:
    print("Starting transaction...")
    cursor.execute("insert into student values(4,'raj', 115,25)")

    print("Creating savepoint sp1...")
    cursor.execute("savepoint sp1")

    try:
        cursor.execute("insert into student values(5,'NANU',116,23)")
        print("Creating savepoint sp2...")
        cursor.execute("savepoint sp2")


    except Exception as e:
        print("Error in second insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")



    try:
        cursor.execute("insert into student values(6,'raj',117,26)")
        print("Second insert successful.")
        print("Creating savepoint sp3...")
        cursor.execute("savepoint sp3")
    except Exception as e:
        print("Error in third insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")



    print("Committing transaction...")
    connection.commit()

except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()