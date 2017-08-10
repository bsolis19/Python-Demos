import mysql.connector as mysql

conn = mysql.connect(user = 'root', password = 'password', host = 'localhost')

print(conn)

conn.close()