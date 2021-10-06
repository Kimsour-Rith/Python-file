import psycopg2
db_conn =None
cursor = None
try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", database= "kit_b9", user= "postgres", password= "zto78")
    print("Connection succeed")
    db_conn.autocommit = False
    cursor = db_conn.cursor()
    print("Cursor received")

    debit_ac = int(input("Input the account to be debited: "))
    credit_ac = int(input("Input the account to be credited: "))
    amt = int(input("Input the amount to be transferred: "))

    cursor.execute("UPDATE customers SET balance = balance - %d WHERE c_id = %s;", (amt, debit_ac))
    print("Successfully debited from account number",debit_ac)
    cursor.execute("UPDATE customers SET balance = balance + %d WHERE c_id = %s;", (amt, credit_ac))
    print("Successfully credited from account number",credit_ac)

    db_conn.commit()
    print("Amount transfer success...")


except Exception as e:
    print("Issue: ",e)
    db_conn.rollback()
    print("Something went wrong rolling back to previous stage, Transaction failed")

finally:
    cursor.close()
    print("Cursor closed")
    db_conn.close()
    print( "Connection closed")