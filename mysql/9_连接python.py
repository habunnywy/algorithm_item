import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '53532628'
)

cursor = connection.cursor()

# 创建资料库
# cursor.execute("CREATE DATABASE `qq`;")

# 展示资料库
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for record in records:
#     print(record)

# 选择资料库
cursor.execute("USE `sql_tutorial`;")

# 创建表格
cursor.execute('CREATE TABLE `qq`(qq INT);')

# 关闭连接
cursor.close()
connection.close()