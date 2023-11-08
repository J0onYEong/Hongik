import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='wnsdudmysql0921', db='university', charset='utf8mb4')
cursor = conn.cursor()

sql = "select * from student"

cursor.execute(sql)

rows = cursor.fetchall()
print(rows)

conn.close()