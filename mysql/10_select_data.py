import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '53532628',
    database = 'sql_tutorial'
)

# 创建游标
cursor = connection.cursor()

# 取得branch表格的资料
cursor.execute("SELECT * FROM `branch`;")
records = cursor.fetchall()
for record in records:
    print(record)


# 关闭连接
cursor.close()
connection.close()
