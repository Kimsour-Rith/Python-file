import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", database= "kit_b9", user= "postgres", password= "zto78")
    print("Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")

    cursor.execute("CREATE TABLE customers (c_id SERIAL, c_name VARCHAR(50), age INTEGER, balance MONEY);") # it won't work unless you commit it after the connection
    db_conn.commit()        # if you don't put commit() it won't show any update
    print("Table created successfully")
except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")