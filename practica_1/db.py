"""
Connects to a SQL database using pyodbc
"""
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
USERNAME = "sa" #os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'

#print("connectionString: " + connectionString)

def select(SQL_QUERY):
    result = None

    try:
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()

        try:
            #print("SQL_QUERY: " + SQL_QUERY)
            cursor.execute(SQL_QUERY)
            result = cursor.fetchall()
        except Exception as error:
            print("select: An exception occurred when execute SQL query. ", error)
        finally:
            cursor.close()
            conn.close()
    except Exception as error2:
        print("select: An exception occurred when connect to SQL Server. ", error2)
    return result

conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

def insert(SQL_STATEMENT):
    result = -1

    try:
        #conn = pyodbc.connect(connectionString)
        #cursor = conn.cursor()

        try:
            print("SQL_STATEMENT: " + SQL_STATEMENT)
            cursor.execute(SQL_STATEMENT)
            conn.commit()
        except Exception as error:
            print("insert: An exception occurred when execute SQL statement. ", error)
        #finally:
            #cursor.close()
            #conn.close()
    except Exception as error2:
        print("insert: An exception occurred when connect to SQL statement. ", error2)
    return result

def bulkInsert(SQL_STATEMENT, data):
    result = -1

    try:
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()

        try:
            print("SQL_STATEMENT: " + SQL_STATEMENT)
            cursor.executemany(SQL_STATEMENT, data)
            conn.commit()
        except Exception as error:
            print("bulkInsert: An exception occurred when execute SQL statement. ", error)
        finally:
            cursor.close()
            conn.close()
    except Exception as error2:
        print("bulkInsert: An exception occurred when connect to SQL statement. ", error2)
    return result

def ddl(SQL_STATEMENT):
    result = -1

    try:
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()

        try:
            #print("SQL_STATEMENT: " + SQL_STATEMENT)
            cursor.execute(SQL_STATEMENT)
            conn.commit()
        except Exception as error:
            print("ddl: An exception occurred when execute SQL statement. ", error)
        finally:
            cursor.close()
            conn.close()
    except Exception as error2:
        print("ddl: An exception occurred when connect to SQL statement. ", error2)
    return result
