import psycopg2
db_conn = None      # create an empty object you can put it or not
try:
    db_conn = psycopg2.connect(host ="localhost", port= "5432", user= "postgres", password= "zto78")
    print("Connection succeed")

except Exception as e:
    print(e)
finally:
    db_conn.close()
    print("Connection closed")