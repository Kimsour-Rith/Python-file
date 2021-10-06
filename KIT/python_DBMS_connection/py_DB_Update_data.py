import psycopg2

try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", database= "boobi_company", user= "postgres", password= "zto78")
    print("Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")


    cursor.execute(''' UPDATE employees SET age = 25 WHERE em_name = 'Kimsour' ''')
    db_conn.commit()
    print("Record updated successfully")

except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")