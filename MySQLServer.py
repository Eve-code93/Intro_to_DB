import mysql.connector
from mysql.connector import errorcode, Error

def create_database():
    try:
        # Establish connection to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='kimjose97!'  # Replace with your MySQL password
        )

        # Create cursor object to execute queries
        cursor = connection.cursor()

        # Create the 'alx_book_store' database if it doesn't already exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(create_db_query)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"MySQL Connector Error: {e}")
    
    except Error as e:
        print(f"General MySQL Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Close the MySQL connection if it's open
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
