import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'alx_book_store'

# Database connection configuration
config = {
    'user': 'root',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create database if it doesn't exist
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    cursor.execute(create_db_query)

    print(f"Database '{DB_NAME}' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Error: Database '{DB_NAME}' does not exist and could not be created.")
    else:
        print(f"Database error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")
