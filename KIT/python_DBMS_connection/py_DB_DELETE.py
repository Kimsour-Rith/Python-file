import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", database= "boobi_company", user= "postgres", password= "zto78")
    print("Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")


    cursor.execute("DELETE FROM employees WHERE em_name = 'Sreylin'")
    db_conn.commit()
    print("Record deleted successfully")
    print(cursor.rowcount, "record(s) deleted")

except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")