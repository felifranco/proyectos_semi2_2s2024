"""
Connects to a SQL database using pyodbc
"""
import pyodbc

SERVER = 'localhost'
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'strong@Password'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT * FROM PermissionType pt 
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.Descripcion}")

