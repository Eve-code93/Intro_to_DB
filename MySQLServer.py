import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',  # Change this to your MySQL server host
            user='root',  # Change this to your MySQL username
            password='kimjose97!'  # Change this to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

