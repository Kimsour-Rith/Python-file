import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect( host ="localhost", port= "5432", user= "postgres", password= "zto78")
    db_conn.autocommit = True
    print( "Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")

    cursor.execute("CREATE DATABASE kit_b9")     # it won't work unless you commit it after the connection
except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")