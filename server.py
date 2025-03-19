from json import load
from mcp.server.fastmcp import FastMCP
import sqlite3
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("AN-SQL-AGENT")

@mcp.tool()
def query_data(sql: str) -> str:
    conn = sqlite3.connect("database.db")
    try:
        result = conn.execute(sql).fetchall()
        conn.commit()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        conn.close()

# @mcp.tool()
#def connect_to_mysql(host=os.environ.get('MYSQL_HOST'), user=os.environ.get('MYSQL_USER'), password=os.environ.get('MYSQL_PASSWORD'), database=os.environ.get('MYSQL_DB'),sql:str):
#     connection = mysql.connector.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=database
#     )
#     if connection.is_connected():
#         print("Connected to MySQL database successfully!")
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         if sql.strip().lower().startswith("select"):
#             result = cursor.fetchall()
#             return "\n".join(str(row) for row in result) if result else "No results found."

#         connection.commit()
#         return f"Query executed successfully: {cursor.rowcount} rows affected."

#     except Error as e:
#         return f"Error: {str(e)}"

#     finally:
#         if cursor:
#             cursor.close()
#         if connection and connection.is_connected():
#             connection.close()  
        

@mcp.prompt()
def example_prompt(code:str)->str:
    return f"Please review this code:\n\n{code}"

if __name__ == "__main__":
    mcp.run(transport="stdio")