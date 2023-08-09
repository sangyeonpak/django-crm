# set up database
# import psycopg2
import mysql.connector

# Connect to postgres
# conn = psycopg2.connect(database="crm", user="username", password="password", host="localhost")
database = mysql.connector.connect(
    host = 'localhost',
    user = 'username',
    passwd = 'password'
)

# Open a cursor to perform database operations
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

# Execute a query
# cur.execute("SELECT * FROM users")

print("All done!")

# Retrieve query results
# records = cur.fetchall()
# print(records)