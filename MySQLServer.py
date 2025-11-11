import mysql.connector

try :
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor]
    if "alx_book_store" in databases :
        print("Database already exsits No changes made.")
    else:
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)

finally:
    if 'cursor' in locals():
        connection.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()