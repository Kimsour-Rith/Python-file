import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", database= "kit_b9", user= "postgres", password= "zto78")
    print("Connection succeed")
    cursor = db_conn.cursor()
    print("Cursor received")

    c_name = input("Input your name: ")
    age = int(input("Input your age: "))
    balance = int(input("Input your balance: "))

    cursor.execute("INSERT INTO customers (c_name, age,balance) VALUES (%s, %s, %s);", (c_name,age,balance))
    db_conn.commit()        # if you don't put commit() it won't show any update
    print("Record inserted successfully")
except Exception as e:
    print("Issue: ",e)
finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")