import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='advance_python',
    autocommit=False
)

cursor = connection.cursor()

try:
    print("Starting transaction...")
    cursor.execute("insert into marksheet values(18, 108, 'raj', 45, 48, 38)")

    print("Creating savepoint sp1...")
    cursor.execute("savepoint sp1")

    try:
        # This will try to insert the second record
        cursor.execute("insert into marksheet values(17, 109, 'raj', 13, 23, 38)")
    except Exception as e:
        # If there's an error in the second insert, rollback to savepoint
        print("Error in second insert, rolling back to savepoint sp1...")
        cursor.execute("rollback to savepoint sp1")

    print("Committing transaction...")
    connection.commit()

except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()