from sqlalchemy import create_engine

# Gather the necessary connection details
username = 'myuser'
password = 'mypassword'
host = 'localhost'
port = '3306'
database_name = 'mydatabase'

# Create the connection string
connection_string = f'mysql://{username}:{password}@{host}:{port}/{database_name}'

# Establish the connection
engine = create_engine(connection_string)

# Use the connection
# You can perform various database operations using the engine object
# For example, you can execute queries, create tables, etc.
# Here's a simple example to fetch data from a table named 'users':
with engine.connect() as connection:
    result = connection.execute('SELECT * FROM users')
    for row in result:
        print(row)
