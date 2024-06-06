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

# 新增一笔资料
cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL);")

# 修改
cursor.execute("UPDATE `branch` SET `manager_id` = NULL WHERE `branch_id` = 4;")

# 删除
# cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")

# 关闭
cursor.close()
connection.commit() # 修改资料库的资料时，需要commit才会生效
connection.close()