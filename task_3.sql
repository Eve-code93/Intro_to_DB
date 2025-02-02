import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish connection to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='your_password_here'  # Replace with your MySQL password
        )

        # Create cursor object to execute queries
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        db_name = "alx_book_store"
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        cursor.execute(create_db_query)

        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure the connection is properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

