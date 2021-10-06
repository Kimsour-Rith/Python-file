import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect(host = "localhost", port = "5432", database = "boobi_company", user = "postgres", password = "zto78")
    print("Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")

    cursor.execute("SELECT * FROM employees;")
    #cursor.execute("SELECT * FROM employees WHERE em_id = 3;")
    records = cursor.fetchall()     # this function is used to show all the record in python
    print(records)

    #first_record = cursor.fetchone()   # is used to show the first record
    #print(first_record)
    print("*"*15)
    for re in records:
        print(re)
except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")